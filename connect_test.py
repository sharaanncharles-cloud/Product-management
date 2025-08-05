import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",  # Change if needed
    database="product_management"
)

# Create a cursor
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM product_managers")

# Fetch all results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Clean up
cursor.close()
connection.close()
