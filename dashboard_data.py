import mysql.connector
import pandas as pd

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Emma@123',
    database='product_management'
)

# 2. Fetch view data
views = [
    'v_feature_summary_by_pm',
    'v_task_status_by_sprint',
    'v_release_features'
]

for view in views:
    df = pd.read_sql(f"SELECT * FROM {view}", conn)
    print(f"\n=== {view} ===")
    print(df.head())

conn.close()
