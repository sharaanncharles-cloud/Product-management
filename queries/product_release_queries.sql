-- All released products
SELECT * FROM products
WHERE release_status = 'Released';

-- Releases by version and date
SELECT product_id, version, release_date
FROM releases
ORDER BY release_date DESC;

-- Count of releases per product
SELECT product_id, COUNT(*) AS release_count
FROM releases
GROUP BY product_id;
