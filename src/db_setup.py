import sqlite3

DB = "data/download_tracker.db"

def setup_database():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS downloads (
            file_id TEXT PRIMARY KEY,
            filename TEXT,
            size INTEGER,
            checksum TEXT,
            download_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB}")

def setup_

def main():
    setup_database()

if __name__ == "__main__":
    main()
