import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emma@123",
    database="product_management"
)

# === Chart 1: Features by Status per PM ===
df1 = pd.read_sql("SELECT * FROM v_feature_summary_by_pm", conn)
pivot1 = df1.pivot_table(index='product_manager', columns='status', values='feature_count', fill_value=0)
pivot1.plot(kind='bar', stacked=True)
plt.title('Feature Count by Status per Product Manager')
plt.xlabel('Product Manager')
plt.ylabel('Feature Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_features_by_pm.png')
plt.clf()

# === Chart 2: Tasks by Status per Sprint ===
df2 = pd.read_sql("SELECT * FROM v_task_status_by_sprint", conn)
pivot2 = df2.pivot_table(index='sprint_name', columns='status', values='task_count', fill_value=0)
pivot2.plot(kind='bar', stacked=True)
plt.title('Task Status per Sprint')
plt.xlabel('Sprint')
plt.ylabel('Task Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_tasks_by_sprint.png')
plt.clf()

# === Chart 3: Features per Release ===
df3 = pd.read_sql("SELECT * FROM v_release_features", conn)
grouped = df3.groupby(['release_name', 'status']).size().unstack(fill_value=0)
grouped.plot(kind='bar', stacked=True)
plt.title('Feature Status per Release')
plt.xlabel('Release')
plt.ylabel('Feature Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_features_per_release.png')
plt.clf()

print("✅ Charts saved as PNG files in the current folder.")
