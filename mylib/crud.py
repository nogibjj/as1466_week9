'''
This file contains basic CRUD operations 
'''
""""
ETL-Query script
"""

import sqlite3


# Your CRUD operation functions
def create(query,  db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def read(query, db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    connection.close()
    return user

def update(query, db_name='LifeDB.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
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

