# flask_app.py
from flask import Flask, request
from telegram import Update
from bot import application as telegram_app, WEBHOOK_SECRET
import asyncio

app = Flask(__name__)

@app.route(f"/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)

    async def process():
        await telegram_app.process_update(update)

    asyncio.run(process())
    return "ok", 200

@app.route("/")
def index():
    return "Hello from Flask!"
