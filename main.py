"""
ETL-Query script
"""
import fire
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.crud import create, read, drop, update 


def main(operation, query_string=None):
    if operation == 'query':
        # Extract
        print("Extracting data...")
        extract()

        # Transform and load
        print("Transforming data...")
        load()

        # Query
        print("Querying data...")
        query(query_string)
    elif operation == 'create': 
        create()
    elif operation == 'drop': 
        drop(query_string)
    elif operation == 'read': 
        read(query_string)
    elif operation == 'update': 
        update(query_string)
        




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ETL and CRUD operations')
    parser.add_argument('operation', nargs='?', default='query', choices=['query', 'create', 'read', 'update', 'delete', 'insert','drop'], help='Operation to perform')
    parser.add_argument('--query_string', help='SQL query string (required for query operation)')
    args = parser.parse_args()
    # Join the provided data as a single string to use as the query
    

    fire.Fire(main)