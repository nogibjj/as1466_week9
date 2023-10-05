"""Query the database"""

import sqlite3
from tabulate import tabulate


def query(the_query):
    """Query the database for all rows of the JeopardyDB table"""
    conn = sqlite3.connect("LifeDB.db")
    cursor = conn.cursor()
    cursor.execute(the_query)
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print(tabulate(rows, headers=column_names))

    
    conn.close()
    return rows
