import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",
    database="product_management"
)
cursor = conn.cursor()

tasks = [
    ("Create login API", "In Progress", "High", date(2025, 8, 1), date(2025, 8, 2), None, 1, 1),
    ("Design landing page", "Backlog", "Medium", date(2025, 8, 1), None, None, 2, 2)
]

cursor.executemany(
    """
    INSERT INTO tasks (description, status, priority, created_at, start_date, completed_at, assigned_to, sprint_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
    tasks
)

conn.commit()
print(f"{cursor.rowcount} tasks inserted.")
conn.close()
