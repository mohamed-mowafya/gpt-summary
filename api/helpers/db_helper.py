import sqlite3

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        return conn
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()