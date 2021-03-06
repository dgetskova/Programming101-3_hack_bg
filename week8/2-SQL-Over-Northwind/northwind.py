# List of names and titles for  all employees 
"""SELECT FirstName, LastName, Title
FROM Employees"""
# List all employees from Seattle.
"""SELECT FirstName, LastName
FROM Employees 
WHERE City LIKE "Seattle""""
# List all employees from London.
"""SELECT FirstName, LastName
FROM Employees 
WHERE City = "Seattle""""
# List all employees that work in the Sales department.
"""SELECT FirstName, LastName
FROM Employees
WHERE Title LIKE "%Sales%""""
# List all females employees that work in the Sales department.
"""SELECT FirstName, LastName
FROM Employees
WHERE Title LIKE "%Sales%" AND (TitleOfCourtesy = "Mr." OR TitleOfCourtesy = "Mrs.")""""
# List the 5 oldest employees.
"""SELECT *
FROM Employees
ORDER BY BirthDay ASC
LIMIT 5"""
# List the first 5 hires of the company.
"""SELECT *
FROM Employees
ORDER BY HireDate ASC
LIMIT 5"""
# List the employee who reports to no one (the boss)
"""SELECT *
FROM Employees
WHERE ReportsTo is NULL"""
# List all employes by their first and last name, and the first and last name of the employees that they report to.
"""SELECT a.FirstName, a.LastName, b.FirstName, b.LastName
FROM Employees a
JOIN Employees b
WHERE a.ReportsTo = b.EmployeeID"""
# Count all female employees.
"""SELECT COUNT(EmployeeID)
FROM Employees
WHERE TitleOfCourtesy = "Mr." OR TitleOfCourtesy = "Mrs.""""
# Count how many employees are there from the different cities. For example, there are 4 employees from London.
"""SELECT COUNT(EmployeeID) AS Count_Persons, City
FROM Employees
GROUP BY City"""
# List all OrderIDs and the shipper name that the order is going to be shipped via.
"""SELECT OrderID, CompanyName
FROM orders
JOIN Shippers
ON Orders.Shipvia = Shippers.ShipperID"""
# List all contries and the total number of orders that are going to be shipped there.
"""SELECT COUNT(OrderID) AS OrdersCount, ShipCountry
FROM Orders
GROUP BY ShipCountry"""
# Find the customer that has placed the most orders.
"""SELECT COUNT(OrderID) AS OrdersCount, FirstName
FROM Orders
JOIN employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY OrdersCount DESC
LIMIT 1"""
# List all orders, with the employee serving them and the customer, that has placed them.
""" SELECT OrderID, ContactName AS Customer_Name, FirstName as Employee_Name
FROM Orders
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID """
