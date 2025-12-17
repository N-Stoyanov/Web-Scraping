-- ====================================================
-- 1. Average price by category
-- ====================================================
SELECT Category, AVG(Price) AS avg_price
FROM books
GROUP BY Category;


-- ====================================================
-- 2. Top 10 most expensive books
-- ====================================================
SELECT Title, Price
FROM books
ORDER BY Price DESC
LIMIT 10;


-- ====================================================
-- 3. Count of books by rating
-- ====================================================
SELECT Rating, COUNT(*) AS count
FROM books
GROUP BY Rating
ORDER BY count DESC;


-- ====================================================
-- 4. Average price by rating
-- ====================================================
SELECT Rating, AVG(Price) AS avg_price
FROM books
GROUP BY Rating
ORDER BY avg_price DESC;


-- ====================================================
-- 5. Books in a specific category over 40
-- ====================================================
SELECT Title, Price, Rating
FROM books
WHERE Category = 'travel_2'
  AND Price > 40;

