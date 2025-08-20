# BUG-001 — CRITICAL — Missing input validation for email in /tour flow

**Project:** Telegram Client Bot  
**Reported by:** Yuliana Y.  
**Date:** 2024-09-19

**Severity:** Critical  
**Environment:** PythonAnywhere deployment, webhook mode, bot version v1.0

**Steps to reproduce:**
1. Open Telegram → start bot `/tour`
2. Proceed to step asking for email address
3. Input: `not-an-email`
4. Press send

**Expected result:** Bot validates email format and prompts user to enter valid email.
**Actual result:** Bot accepts invalid email, forwards data to manager; downstream processing fails and raises server-side exception.

**Evidence:** `GetWebhookInfo.png` (linked) + Postman request trace (see `postman_collection.log`)

**Suggested fix:** Add server-side email validation (regex) + client-side check before sending + return user-friendly message.

**Status:** Open
