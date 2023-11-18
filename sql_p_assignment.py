-- Create a table
CREATE TABLE RandomTable (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    City VARCHAR(100)
);

-- Insert some random data
INSERT INTO RandomTable (ID, Name, Age, City)
VALUES
    (1, 'John Doe', 25, 'New York'),
    (2, 'Jane Smith', 30, 'Los Angeles'),
    (3, 'Bob Johnson', 22, 'Chicago'),
    (4, 'Alice Williams', 28, 'San Francisco');

-- Update some records
UPDATE RandomTable
SET Age = Age + 1
WHERE City = 'New York';

-- Select data
SELECT * FROM RandomTable
WHERE Age > 25;

-- Create another table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Quantity INT,
    OrderDate DATE
);

-- Insert some random order data
INSERT INTO Orders (OrderID, ProductName, Quantity, OrderDate)
VALUES
    (101, 'Laptop', 3, '2023-01-15'),
    (102, 'Smartphone', 5, '2023-02-20'),
    (103, 'Headphones', 2, '2023-03-10'),
    (104, 'Tablet', 1, '2023-04-05');

-- Join tables to retrieve information
SELECT RandomTable.Name, Orders.ProductName, Orders.Quantity
FROM RandomTable
JOIN Orders ON RandomTable.ID = Orders.OrderID
WHERE RandomTable.Age > 25;

-- Calculate total order quantity
SELECT ProductName, SUM(Quantity) AS TotalQuantity
FROM Orders
GROUP BY ProductName;

-- Delete records older than a specific date
DELETE FROM Orders
WHERE OrderDate < '2023-03-01';
