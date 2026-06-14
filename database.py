import sqlite3
import os
from datetime import date

DB_PATH = os.getenv('DB_PATH', 'birthdays.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            category TEXT DEFAULT 'friends',
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_today_birthdays():
    today = date.today()
    conn = get_connection()
    cur = conn.cursor()
    # Сравниваем месяц и день, игнорируя год
    cur.execute('''
        SELECT name, category, email 
        FROM contacts 
        WHERE strftime('%m', birth_date) = ? AND strftime('%d', birth_date) = ?
    ''', (today.strftime('%m'), today.strftime('%d')))
    rows = cur.fetchall()
    conn.close()
    return rows