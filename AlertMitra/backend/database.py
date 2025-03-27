import sqlite3

DB_PATH = "database/chatbot.db"

# Connect to Database
def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Create Tables
def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as schema_file:
        cursor.executescript(schema_file.read())

    conn.commit()
    conn.close()

# Insert Chat Messages
def save_chat(user_id, message, response):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_id, message, response) VALUES (?, ?, ?)",
                   (user_id, message, response))
    conn.commit()
    conn.close()

# Fetch Chat History
def get_chat_history(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT message, response, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC",
                   (user_id,))
    chats = cursor.fetchall()
    conn.close()
    return chats

# Insert Disaster Alert
def create_alert(title, description, location, severity):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO disaster_alerts (title, description, location, severity) VALUES (?, ?, ?, ?)",
                   (title, description, location, severity))
    conn.commit()
    conn.close()

# Fetch All Disaster Alerts
def get_alerts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM disaster_alerts ORDER BY timestamp DESC")
    alerts = cursor.fetchall()
    conn.close()
    return alerts

if __name__ == "__main__":
    create_tables()
    print("✅ Database setup completed!")
