import os
import psycopg2
import csv

PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")
EXPORT_PATH = os.getenv("EXPORT_PATH", "/data/shipments.csv")

conn = psycopg2.connect(
    host=PG_HOST,
    port=PG_PORT,
    user=PG_USER,
    password=PG_PASSWORD,
    dbname=PG_DATABASE
)
cur = conn.cursor()
cur.execute("SELECT * FROM shipments")
with open(EXPORT_PATH, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([desc[0] for desc in cur.description])  # Write headers
    writer.writerows(cur.fetchall())
cur.close()
conn.close()
print(f"Exported shipments to {EXPORT_PATH}")
