import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        customer TEXT,
        amount INTEGER,
        date TEXT
    )
    """)

    data = [
        ("Alice", 200, "2024-01-01"),
        ("Bob", 150, "2024-01-02"),
        ("Alice", 300, "2024-01-03"),
        ("Charlie", 400, "2024-01-04")
    ]

    cursor.executemany(
        "INSERT INTO sales (customer, amount, date) VALUES (?, ?, ?)", data
    )

    conn.commit()
    conn.close()
