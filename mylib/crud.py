'''
This file contains basic CRUD operations 
'''
""""
ETL-Query script
"""

import sqlite3
import pandas as pd
from tabulate import tabulate

# Your CRUD operation functions
def create(database_Name = 'LifeDB.db'):
    con = sqlite3.connect(database_Name)
    df = pd.read_csv("data/life_expectancy.csv")

    df.to_sql("life_expectancy", con, if_exists="replace", index=False)

    # cursor = con.execute("SELECT * FROM universities")
    # result = cursor.fetchall()
    con.commit()
    con.close()

    return "Table named life_expectancy created"

def read(query, db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    print(user)
    connection.close()
    return user



def update(query, db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Execute the update query
    cursor.execute(query)
    connection.commit()

    # Commit the changes to the database
    
    

    # Parse the table name and condition from the update query
    # This assumes that the query contains "UPDATE table_name SET ... WHERE condition"
    table_name = query.split('UPDATE')[1].split('SET')[0].strip()
    condition = query.split('WHERE')[1].strip()

    # Execute a SELECT query to retrieve the updated record
    select_query = f"SELECT * FROM {table_name} WHERE {condition}"
    cursor.execute(select_query)
    updated_record = cursor.fetchone()
    print(updated_record)
    connection.commit()
    

    # Print the updated record
    if updated_record:
        return "Record Updated", updated_record
    else:
        return "Record Not Found", None
    
    
    connection.close()


def delete(query, db_name='lifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def insert(query,  db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def drop (query, db_name = 'LifeDB.db'): 
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


