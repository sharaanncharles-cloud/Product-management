import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",
    database="product_management"
)

cursor = conn.cursor()

# Insert a new feature into the features table
sql = """
INSERT INTO features (title, description, status, pm_id)
VALUES (%s, %s, %s, %s)
"""
values = ("Analytics Dashboard", "Provides user behavior insights", "Backlog", 1)

cursor.execute(sql, values)
conn.commit()

print(f"Inserted feature ID: {cursor.lastrowid}")

# Close the connection
cursor.close()
conn.close()
