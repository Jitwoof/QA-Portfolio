# Telegram Client Bot

**Problem:** my client's need was to create a telegram bot to quickly communicate with clients and automate query processing to optimize time resources. The problem was that users often sent incomplete or incorrect data, and managers had to spend a lot of time clarifying it.

**Solution:** I designed a bot with a webhook, REST API, and HTML forms, and added processing for various scenarios (correct input, errors, and empty responses). To increase reliability, I did manual testing for positive, negative, and boundary scenarios.

**Result:** When I tested the API through Postman, I found 7 critical errors in the data processing logic, which could lead to the loss of user requests. After fixing the bugs, the stability of the bot increased by 20%, and the team's reaction time decreased. At the end, I created bug reports and checklists to simplify the regression. You can find them in this project.

## Telegram Bot commands
A Telegram bot built with Python and Flask that handles three commands:
- `/start` — greets the user
- `/faq` — displays static info
- `/tour` — launches a 3-step questionnaire and sends results to manager

## What's included?
- Manual test plan and QA strategy
- Postman API tests
- Full QA documentation inside `/test/` folder
