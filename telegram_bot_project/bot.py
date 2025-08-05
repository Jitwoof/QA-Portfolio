import asyncio
import logging
import os
import re
from pathlib import Path

from dotenv import load_dotenv

from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, Update)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, MessageHandler, filters)

# =================================================================================
# 1. CONFIGURATION
# =================================================================================
load_dotenv()

# These values are read from environment variables on PythonAnywhere
TOKEN = 'BOT-TOKEN'
MANAGER_CHAT_ID = 'CHAT-ID'

# --- IMPORTANT ---
WEBHOOK_SECRET = "SECRET"
WEBAPP_URL = "https://@.pythonanywhere.com"

# Create a folder for logs if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logs/bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# =================================================================================
# 2. HELPER & HANDLER FUNCTIONS
# =================================================================================

def escape_markdown_v2(text: str) -> str:
    """Escapes special characters for Telegram MarkdownV2."""
    if not isinstance(text, str):
        text = str(text)
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)


async def send_to_manager(user_info: dict, app: Application):
    """Sends user application to the manager with proper formatting."""
    try:
        # Escape all user-provided data for MarkdownV2
        user_first_name = escape_markdown_v2(user_info.get('first_name', ''))
        username = escape_markdown_v2(user_info.get('username', 'нет'))
        direction = escape_markdown_v2(user_info.get('direction', ''))
        dates = escape_markdown_v2(user_info.get('dates', ''))
        budget = escape_markdown_v2(user_info.get('budget', ''))

        # CORRECTED: Changed \! to \\! to be valid Python syntax.
        # Python will process \\! into the string \! which is what Telegram needs.
        message = f"""🚀 *Новая заявка на тур\\!*

👤 *Клиент:* [{user_first_name}](tg://user?id={user_info['id']})
📱 @{username}

📍 *Направление:* {direction}
📅 *Даты:* {dates}
💰 *Бюджет:* {budget}"""

        await app.bot.send_message(
            chat_id=MANAGER_CHAT_ID,
            text=message,
            parse_mode="MarkdownV2",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "💬 Написать клиенту",
                    url=f"tg://user?id={user_info['id']}"
                )
            ]])
        )
        logger.info(f"Successfully sent application for user {user_info['id']} to manager.")
    except Exception as e:
        logger.error(f"Failed to send application for user {user_info['id']} to manager. Error: {e}")
        logger.error(f"User data that caused the error: {user_info}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcomes the user."""
    await update.message.reply_text(
        "✈️ Добро пожаловать в бот для подбора туров!\n"
        "Используйте /tour для подбора или /faq для помощи"
    )


async def tour(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the tour application process."""
    user = update.message.from_user
    context.user_data['tour'] = {
        'step': 1,
        'id': user.id,
        'first_name': user.first_name,
        'username': user.username or 'нет'
    }
    await update.message.reply_text(
        "Давайте подберём тур! Ответьте на 3 вопроса:\n\n"
        "1. Куда хотите поехать? (Например: Турция, Бали)"
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles user answers for the tour application."""
    tour_data = context.user_data.get('tour')
    if not tour_data:
        await update.message.reply_text("Пожалуйста, начните с команды /tour, чтобы я мог вам помочь.")
        return

    text = update.message.text
    step = tour_data.get('step')

    if step == 1:
        tour_data['direction'] = text
        tour_data['step'] = 2
        await update.message.reply_text("2. На какие даты? (Например: 01-15 августа)")
    elif step == 2:
        tour_data['dates'] = text
        tour_data['step'] = 3
        await update.message.reply_text("3. Какой у вас бюджет на человека? (Например: 100 000 рублей)")
    elif step == 3:
        tour_data['budget'] = text
        await update.message.reply_text(
            "✅ Спасибо! Ваша заявка принята.\n"
            "Менеджер свяжется с вами в течение часа."
        )
        # Pass the application instance from the context
        await send_to_manager(tour_data, context.application)
        context.user_data.pop('tour', None)


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows FAQ options."""
    keyboard = [
        [InlineKeyboardButton("💳 Оплата", callback_data="faq_pay")],
        [InlineKeyboardButton("❌ Отмена тура", callback_data="faq_cancel")],
        [InlineKeyboardButton("📞 Контакты", callback_data="faq_contacts")]
    ]
    await update.message.reply_text(
        "ℹ Выберите вопрос:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles FAQ button presses."""
    query = update.callback_query
    await query.answer()

    faq_messages = {
        "faq_pay": "💳 *Способы оплаты:*\n\\- Картой онлайн\n\\- Наличными в офисе\n\\- По реквизитам через банк",
        "faq_cancel": "❌ *Условия отмены:*\n\\- Без штрафа при отмене за 14 дней\n\\- 50% возврат при отмене за 7 дней\n\\- Менее 7 дней до поездки \\- стоимость не возвращается",
        "faq_contacts": "📞 *Контакты:*\n\\- Менеджер: @your\\_manager\\_username\n\\- Телефон: `+7 (XXX) XXX-XX-XX`\n\\- Email: support@yourcompany\\.com"
    }

    if query.data in faq_messages:
        await query.edit_message_text(text=faq_messages[query.data], parse_mode="MarkdownV2")


# =================================================================================
# 3. APPLICATION SETUP
# =================================================================================
# The WSGI server on PythonAnywhere will import this 'application' object.
# We don't need a main() function or a polling loop.

if not TOKEN:
    logger.critical("FATAL: TELEGRAM_TOKEN environment variable not set!")
else:
    # Create the Application instance
    application = Application.builder().token(TOKEN).build()

    # Register all the handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tour", tour))
    application.add_handler(CommandHandler("faq", faq))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    asyncio.run(application.initialize())

    # =================================================================================
# 4. LOCAL POLLING STARTUP (NEWLY ADDED)
# =================================================================================
# This block will only run when you execute `python bot.py` directly.
# It will NOT run when PythonAnywhere imports your file.

if __name__ == "__main__":
    if application:
        logger.info("Starting bot in polling mode...")
        application.run_polling()
