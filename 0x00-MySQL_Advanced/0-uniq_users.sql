-- creating the table users if not exist
-- it have id(int), email(varch(255), not null) and name(varch(255))
CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
