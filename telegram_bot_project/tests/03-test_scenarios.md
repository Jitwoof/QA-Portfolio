
# Test Scenarios — Telegram Client Bot

This document lists test scenarios that will be covered during manual and API testing of the Telegram Client Bot. The bot responds to user commands and guides them through a short questionnaire, then sends the results to a manager.

---

## 🔹 Scenario Group: /faq Command

### TS-01 — Display static FAQ message

- **Precondition:** Bot is running and user opens Telegram
- **Steps:**
  1. User types `/faq`
  2. Bot responds with a predefined FAQ message
- **Expected Result:**  
  - The message is informative and well-formatted  
  - No crashes or errors  
  - Bot does not expect further input

---

## 🔹 Scenario Group: /tour Command (Survey)

### TS-02 — Full survey flow with valid input

- **Steps:**
  1. User types `/tour`
  2. Bot asks question 1: Name
  3. User replies with name
  4. Bot asks question 2: Email
  5. User replies with a valid email
  6. Bot asks question 3: What kind of tour are you interested in?
  7. User replies with free-form text
  8. Bot sends summary to the manager (admin) and confirms completion to user
- **Expected Result:**  
  - All questions appear in correct order  
  - User input is accepted and processed  
  - Summary is sent to manager and user sees confirmation  

---

### TS-03 — Survey interrupted in the middle

- **Steps:**
  1. User starts `/tour`
  2. Provides answer to question 1
  3. Closes chat or becomes inactive
- **Expected Result:**  
  - Bot waits for input indefinitely or cancels after timeout (if implemented)
  - No crash or error
  - No message sent to the manager

---

### TS-04 — Survey submitted with empty answers

- **Steps:**
  1. User types `/tour`
  2. User skips one or more questions (e.g., sends empty message)
- **Expected Result:**  
  - Bot either accepts empty input or asks again (depends on implementation)
  - Summary is still generated
  - Admin receives the submission
  - User sees completion message

---

### TS-05 — Invalid email format

- **Steps:**
  1. User starts `/tour`
  2. Provides name
  3. Enters invalid email (`"test.com"` or `"@gmail"`)
- **Expected Result:**  
  - Bot detects invalid email and asks user to re-enter
  - Only continues once valid email format is given

---

## 🔹 Scenario Group: General Stability

### TS-06 — Bot handles unknown command

- **Steps:**
  1. User types `/helpmeplease`
- **Expected Result:**  
  - Bot replies with a fallback message (“Unknown command” or similar)

---

### TS-07 — Server or webhook is down

- **Steps:**
  1. Webhook is not connected (simulate by removing it or server down)
  2. User sends any command
- **Expected Result:**  
  - User does not receive reply
  - Telegram logs show failed webhook with status 404/500
  - Issue is detectable via `getWebhookInfo`

---

## 🔹 Scenario Group: API Testing (via Postman)

### TS-08 — Send message via Telegram API

- **Steps:**
  1. Use Postman to send `POST` request to `sendMessage`
  2. Provide `chat_id` and `text`
- **Expected Result:**  
  - Message appears in chat  
  - Response code is 200 OK

### TS-09 — Check webhook info

- **Steps:**
  1. Use Postman to send `GET` request to `/getWebhookInfo`
- **Expected Result:**  
  - Response includes correct URL, IP, pending count, etc.  
  - No error message

---

Author: Telegram Client Bot
Version: 1.0
