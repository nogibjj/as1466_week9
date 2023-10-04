"""
Transforms and Loads data into the local SQLite3 database
Example:
"Show Number", "Air Date", "Round", "Category", "Value", "Question", "Answer"
"""
import sqlite3
import pandas as pd


def load():
    dataset = "data/life_expectancy.csv"
    df = pd.read_csv(dataset)
    ## transforming database with Pandas 
    column_mapping = {'Country Name': 'Country_name', 'Country Code': 'Country_code','Life Expectancy World Bank':'life_expectancy','Prevelance of Undernourishment':'undernourish',
                  'Health Expenditure %':'health_exp'}
    df = df.rename(columns=column_mapping)
    df = df.iloc[:,:9]
    database_path = "/workspaces/as1466_sqlite_lab/LifeDB.db"
    connect = sqlite3.connect(database_path)
   
    df.to_sql("table1", connect, if_exists="replace", index=False)
    cursor = connect.cursor()
    #cursor.execute(the_query)
    connect.commit()
    connect.close()
  
