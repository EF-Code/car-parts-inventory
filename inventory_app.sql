CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    material VARCHAR(255),
    quantity INT,
    sales_price FLOAT,
    purchase_price FLOAT
);
