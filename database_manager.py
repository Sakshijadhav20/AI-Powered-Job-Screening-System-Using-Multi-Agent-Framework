# database_manager.py

import sqlite3

class DatabaseManager:
    def __init__(self, db_name="candidates.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS candidates
                             (name TEXT, score REAL, email_sent INTEGER)''')
        self.conn.commit()

    def insert_candidate(self, name, score):
        self.conn.execute("INSERT INTO candidates (name, score, email_sent) VALUES (?, ?, ?)", (name, score, 0))
        self.conn.commit()

    def fetch_all_candidates(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM candidates")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
