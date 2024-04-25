-- thsi is to create another user table
--In and not out


CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AOUT_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('CO','US','TN') DEFAULT 'US' 
    );