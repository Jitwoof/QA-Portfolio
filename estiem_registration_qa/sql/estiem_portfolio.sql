CREATE DATABASE IF NOT EXISTS estiem_db;
USE estiem_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS event_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    event_id INT,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (first_name, last_name, email, phone_number) VALUES
('Eger', 'Malik', 'malik@example.com', '1234567890'),
('Izmir', 'Yuildiz', 'izmir@example.com', '9876543210');

INSERT INTO event_registrations (user_id, event_id) VALUES
(1, 101),
(2, 101),
(1, 102);

-- Test queries

SELECT id, first_name, last_name, email, created_at
FROM users
WHERE email = 'alice@example.com';

-- Select all registrations for event 101
SELECT u.first_name, u.last_name, u.email, e.event_id, e.registered_at
FROM event_registrations e
JOIN users u ON e.user_id = u.id
WHERE e.event_id = 101;

-- Attempt duplicate email insert (should fail)
INSERT INTO users (first_name, last_name, email, phone_number)
VALUES ('Charlie', 'Brown', 'alice@example.com', '5555555555');
