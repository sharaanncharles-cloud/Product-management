-- 1. List all customers
SELECT * FROM customers;

-- 2. List all products
SELECT * FROM products;

-- 3. List all orders
SELECT * FROM orders;

-- 4. List all order items
SELECT * FROM order_items;

-- 5. Get customer names and their orders
SELECT 
    c.customer_id, 
    c.customer_name, 
    o.order_id, 
    o.order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;

-- 6. Get order details with product names
SELECT 
    o.order_id, 
    p.product_name, 
    oi.quantity
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- 7. Total amount spent by each customer
SELECT 
    c.customer_name, 
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_name;

-- 8. Most ordered product
SELECT 
    p.product_name, 
    SUM(oi.quantity) AS total_ordered
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_ordered DESC
LIMIT 1;

-- 9. Products not ordered
SELECT 
    product_id, 
    product_name
FROM products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id FROM order_items
);

-- 10. Top 3 customers by total spending
SELECT 
    c.customer_name, 
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 3;
