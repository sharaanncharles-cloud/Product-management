import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",
    database="product_management"
)

cursor = conn.cursor()

sprint_features = [
    (7, 5),  # Sprint 3 → Feature 5
    (8, 6)   # Sprint 4 → Feature 6
]

cursor.executemany(
    "INSERT INTO sprint_features (sprint_id, feature_id) VALUES (%s, %s)",
    sprint_features
)

conn.commit()
print(f"{cursor.rowcount} rows inserted into sprint_features.")

cursor.close()
conn.close()
