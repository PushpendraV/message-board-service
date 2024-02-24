import sqlite3

# Function to create SQLite database and messages table
def create_database():
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Function to insert a new message into the database
def insert_message(message):
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO messages (message) VALUES (?)
    ''', (message,))
    connection.commit()
    connection.close()

# Function to retrieve all messages from the database
def get_messages():
    connection = sqlite3.connect('messages.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    connection.close()
    return messages

# Initialize the database
create_database()
