"""
Usage: python example.py '["prefect"]'
"""

import datetime
import json
import sqlite3
import sys

def create_tables(connection):
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text
                                        CHECK(length("name") >= 4)
                                    ); """

    cur = connection.cursor()
    cur.execute(sql_create_projects_table)
    connection.commit()

def add_project(connection, name):
    sql = '''INSERT INTO projects(name,begin_date)
              VALUES(?,?) '''
    cur = connection.cursor()
    cur.execute(sql, (name, str(datetime.datetime.utcnow())))
    connection.commit()
    return cur.lastrowid

def main(project_names, db_file="/tmp/example.db"):
    connection = sqlite3.connect(db_file) 
    create_tables(connection) 

    for name in project_names:
        add_project(connection, name)

if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
