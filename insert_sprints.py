import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Emma@123',
    database='product_management'
)
cursor = conn.cursor()

# Insert sprints
sprints = [
    ("Sprint 3", "2025-08-01", "2025-08-15"),
    ("Sprint 4", "2025-08-16", "2025-08-30")
]

cursor.executemany(
    "INSERT INTO sprints (name, start_date, end_date) VALUES (%s, %s, %s)",
    sprints
)

conn.commit()
print(f"{cursor.rowcount} sprints inserted.")
cursor.close()
conn.close()
