import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Emma@123',
    database='product_management'
)
cursor = conn.cursor()

# Insert new features
features = [
    ("Bug Fix: Payment Failure", "Fix the critical payment processing bug", "In Progress", 1),
    ("Live Chat Support", "Implement live chat for user support", "Pending", 2)
]

cursor.executemany(
    "INSERT INTO features (title, description, status, pm_id) VALUES (%s, %s, %s, %s)",
    features
)

conn.commit()
print(f"{cursor.rowcount} features inserted.")
cursor.close()
conn.close()
