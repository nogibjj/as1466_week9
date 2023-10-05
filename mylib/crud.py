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
    #conn.isolation_level = None
    connection = sqlite3.connect(db_name)
    connection.isolation_level = None
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
    
    df = pd.read_sql_query(select_query, connection)

    # Close the database connection
    connection.close()

    # Make changes to the DataFrame (if needed)
    # For example, you can manipulate the DataFrame here

    # Connect to the same SQLite database again
    conn = sqlite3.connect(db_name)

    # Write the DataFrame back to a table in the same database
    new_table_name = table_name
    df.to_sql(new_table_name, conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()
    
    
    

    # Print the updated record
    if updated_record:
        return "Record Updated", updated_record
    else:
        return "Record Not Found", None
    
    
    connection.close()


def delete(query, db_name='LifeDB.db'):
    
    connection = sqlite3.connect(db_name)
    connection.isolation_level = None
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()
    connection.close()
    print ('Entry deleted')
    return 'Entry deleted'

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


