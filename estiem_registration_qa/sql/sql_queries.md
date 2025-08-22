## Introduction

During the ESTIEM project, part of the QA responsibilities was to validate data consistency, check correctness of registration forms, and verify integration with the database. Below are SQL queries that were applied to validate different test scenarios.


## 1. Check if new user registration is stored in DB

```sql
SELECT id, first_name, last_name, email, created_at
FROM users
WHERE email = 'testuser@example.com';
```

**Expected Result:**

* One row returned with correct first/last name and email.
* `created_at` timestamp matches registration time.


## 2. Verify uniqueness of email (no duplicates allowed)

```sql
SELECT email, COUNT(*) as count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**Expected Result:**

* Query returns **0 rows**.
* If any rows appear → duplicate registration exists (bug).


## 3. Validate that all registered users are linked to at least one event

```sql
SELECT u.id, u.first_name, u.last_name
FROM users u
LEFT JOIN event_registrations er ON u.id = er.user_id
WHERE er.user_id IS NULL;
```

**Expected Result:**

* Query returns **0 rows**.
* If results exist → users registered in system but not assigned to any event (potential integration issue).


## 4. Check event capacity limits (e.g., max 100 participants)

```sql
SELECT event_id, COUNT(user_id) AS participants
FROM event_registrations
GROUP BY event_id
HAVING COUNT(user_id) > 100;
```

**Expected Result:**

* No events should exceed 100 participants.


## 5. Validate data format for phone numbers

```sql
SELECT id, phone_number
FROM users
WHERE phone_number NOT REGEXP '^[0-9]{10,15}$';
```

**Expected Result:**

* Query should return **0 rows**.
* Any row here indicates invalid phone format (bug in validation).


## 6. Verify that deleted users are marked as inactive, not physically removed

```sql
SELECT id, email, status
FROM users
WHERE status = 'inactive';
```

**Expected Result:**

* Users who requested account deletion appear with `status = inactive`.
* No physical removal of user rows.


## 7. Cross-check API response vs DB values (consistency check)

*(Example: verifying user info returned by API matches database record)*

SQL:

```sql
SELECT first_name, last_name, email
FROM users
WHERE id = 12345;
```

API Response:

```json
{
  "id": 12345,
  "first_name": "Eger",
  "last_name": "Malik",
  "email": "malik@example.com"
}
```

**Expected Result:**

* All fields match 1-to-1.
* Any mismatch reported as defect.


## Conclusion

These SQL queries helped ensure **data integrity, consistency, and correct registration logic** in the ESTIEM system. They were used regularly during regression cycles and load testing validation.
