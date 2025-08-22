# SQL Queries for ESTIEM Registration System

This document contains example SQL queries that were used to validate the correctness of data in the registration system.
Queries cover duplicates detection, filtering by dates, aggregation, and joining related tables.


### 1. Retrieve all registrations

```sql
SELECT * 
FROM event_registrations
LIMIT 20;
```

### 2. Check for duplicate email addresses

```sql
SELECT email, COUNT(*) AS duplicate_count
FROM users
GROUP BY email
HAVING duplicate_count > 1;
```

### 3. Get all registrations for a specific event

```sql
SELECT r.id, u.first_name, u.last_name, r.event_name, r.registration_date
FROM event_registrations r
JOIN users u ON r.user_id = u.id
WHERE r.event_name = 'Leadership Summit';
```

### 4. Count registrations per event

```sql
SELECT event_name, COUNT(*) AS total_registrations
FROM event_registrations
GROUP BY event_name
ORDER BY total_registrations DESC;
```

### 5. Filter registrations by date range

```sql
SELECT *
FROM event_registrations
WHERE registration_date BETWEEN '2024-09-01' AND '2024-09-30';
```

### 6. Find users registered for multiple events

```sql
SELECT u.id, u.first_name, u.last_name, COUNT(r.event_name) AS events_count
FROM users u
JOIN event_registrations r ON u.id = r.user_id
GROUP BY u.id, u.first_name, u.last_name
HAVING events_count > 1;
```

### 7. Check latest registrations (last 10)

```sql
SELECT *
FROM event_registrations
ORDER BY registration_date DESC
LIMIT 10;
```
