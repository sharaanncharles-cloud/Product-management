import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",
    database="product_management"
)
cursor = conn.cursor()

team_members = [
    ("John Doe", "Backend Developer", "john.doe@example.com"),
    ("Jane Smith", "Frontend Developer", "jane.smith@example.com")
]

cursor.executemany(
    "INSERT INTO team_members (name, role, email) VALUES (%s, %s, %s)",
    team_members
)

conn.commit()
print(f"{cursor.rowcount} team members inserted.")
conn.close()
