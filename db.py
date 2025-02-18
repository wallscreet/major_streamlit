import sqlite3

# Initialize database
def init_db():
    conn = sqlite3.connect("assets/notes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to add note
def add_note(content):
    conn = sqlite3.connect("assets/notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

# Function to fetch all notes
def get_notes():
    conn = sqlite3.connect("assets/notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    conn.close()
    return notes if notes else []