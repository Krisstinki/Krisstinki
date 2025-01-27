CREATE DATABASE StorageBackend;
USE StorageBackend;

-- таблица пользователей
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('user', 'admin') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- таблица товаров
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- таблица заказов
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- таблица позиций в заказе
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- тестовые данные
INSERT INTO users (username, password_hash, email, role) VALUES
('admin', 'hashedpassword123', 'admin@example.com', 'admin'),
('user1', 'hashedpassword456', 'user1@example.com', 'user');

INSERT INTO products (name, description, price, stock) VALUES
('Laptop', 'High-performance laptop.', 1200.99, 10),
('Mouse', 'Wireless mouse.', 25.50, 50),
('Keyboard', 'Mechanical keyboard.', 45.75, 30);

INSERT INTO orders (user_id, total_price) VALUES
(2, 1250.99);

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 1200.99),
(1, 2, 2, 25.00);
