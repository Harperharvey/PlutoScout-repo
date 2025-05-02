import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('scout_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        result TEXT
    )''')
    conn.commit()
    conn.close()

def log_scout_result(data):
    conn = sqlite3.connect('scout_logs.db')
    c = conn.cursor()
    timestamp = datetime.utcnow().isoformat()
    result = str(data)
    c.execute("INSERT INTO logs (timestamp, result) VALUES (?, ?)", (timestamp, result))
    conn.commit()
    conn.close()

def get_scout_logs():
    conn = sqlite3.connect('scout_logs.db')
    c = conn.cursor()
    c.execute("SELECT timestamp, result FROM logs ORDER BY timestamp DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return [{"timestamp": r[0], "result": r[1]} for r in rows]

# Run on first boot
init_db()
