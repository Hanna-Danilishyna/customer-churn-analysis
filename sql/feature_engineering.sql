DROP TABLE IF EXISTS customer_features;
CREATE TABLE customer_features AS
SELECT customer_id,
    COUNT(DISTINCT invoice) AS total_orders,
    SUM(quantity) AS total_items,
    SUM(quantity * price) AS total_revenue,
    AVG(quantity * price) AS avg_order_value,
    MAX(invoicedate) AS last_purchase_date,
    MIN(invoicedate) AS first_purchase_date
FROM transactions
WHERE customer_id IS NOT NULL
GROUP BY customer_id;