"""Create the demo login. Run after schema.sql and backend dependencies are installed."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))
from db import get_connection
from auth import hash_password
conn=get_connection();cur=conn.cursor()
try:
    cur.execute('INSERT INTO users(username,email,password_hash) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE password_hash=VALUES(password_hash)',('admin','admin@example.com',hash_password('admin123')))
    conn.commit();print('Demo user ready: admin / admin123')
finally:cur.close();conn.close()
