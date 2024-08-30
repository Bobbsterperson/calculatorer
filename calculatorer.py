import re
import sqlite3


def initialize_database(db_name="results.db"):
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_value REAL,
        result_value REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def insert_result(input_value, result_value):
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO results (input_value, result_value)
    VALUES (?, ?)
    ''', (input_value, result_value))
    conn.commit()
    conn.close()

def print_from_db():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM results')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def calc(n):
    validations(n)
    try:
        result = eval(n)
        print(result)
        return result
    except NameError as e:
        raise ValueError(f"Invalid expression with undefined variable: {str(e)}")
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")


def validations(expression):
    if "," in expression:
        raise ValueError("no ',' pls")
    elif "(" in expression and ")" not in expression:
        raise ValueError("open '(' but not closed")
    elif ")" in expression and "(" not in expression:
        raise ValueError("closed ')' but not opened")
    elif "**" in expression or "//" in expression:
        pass
    elif re.search(r'[\+\-\*/]{2,}', expression):
        raise ValueError("more than one operator")
    elif "]" in expression or "[" in expression or "{" in expression or "}" in expression:
        raise ValueError("no brackets pls")
    elif "/ 0" in expression or "// 0" in expression:
        raise ZeroDivisionError("division by zero error")


initialize_database()
if __name__ == "__main__":
    the_input = input()
    result = calc(the_input)
    insert_result(the_input, result)
    print_from_db()
