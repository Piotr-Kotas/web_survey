# populate_queries.py

import sqlite3

DATABASE = './data/site.db'

def populate_queries():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    with open('data/questions.txt', 'r') as file:
        questions = file.readlines()
        for question in questions:
            cursor.execute("INSERT INTO queries (question) VALUES (?)", (question.strip(),))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_queries()
