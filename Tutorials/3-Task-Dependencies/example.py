"""
Usage: python example.py '["prefect"]'
"""

from asyncio import wait_for
import datetime
import json
import sqlite3
import sys
from prefect import flow, task

@task
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

@task
def add_project(connection, name):
    sql = '''INSERT INTO projects(name,begin_date)
              VALUES(?,?) '''
    cur = connection.cursor()
    cur.execute(sql, (name, str(datetime.datetime.utcnow())))
    connection.commit()
    return cur.lastrowid

@flow(name="Add projects to DB")
def main(project_names, db_file="/tmp/example.db"):
    # prefect may switch threads
    connection = sqlite3.connect(db_file, check_same_thread=False) 
    table_task = create_tables(connection)

    for name in project_names:
        add_project(connection, name, wait_for=[table_task])

if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
