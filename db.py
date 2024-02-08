

'''
This  caters to database management capabilities within a Flask application, using SQLite. It facilitates database 
connection handling ensuring that the application can interact with its database effectively. 
'''

import click
import os
import sqlite3
from flask import current_app, g

# Establishes a connection to the database and enables foreign key support
def get_db_con(pragma_foreign_keys=True):
    if 'db_con' not in g:
        # Creates a database connection and stores it in Flask's application context
        g.db_con = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db_con.row_factory = sqlite3.Row
        # Enables foreign key constraints if specified
        if pragma_foreign_keys:
            g.db_con.execute('PRAGMA foreign_keys = ON;')
    return g.db_con

# Closes the database connection
def close_db_con(e=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        db_con.close()

@click.command('init-db')
def init_db():
    # Initializes the database by creating necessary tables from a script
    try:
        # Ensures the instance folder exists
        os.makedirs(current_app.instance_path)
    except OSError:
        pass
    db_con = get_db_con()
    # Executes the script to drop existing tables
    with current_app.open_resource('sql/drop_tables.sql') as f:
        db_con.executescript(f.read().decode('utf8'))
    # Executes the script to create new tables
    with current_app.open_resource('sql/create_tables.sql') as f:
        db_con.executescript(f.read().decode('utf8'))
    click.echo('Database has been initialized.')

# Inserts sample data into the database
def insert_sample():
    db_con = get_db_con()
    with current_app.open_resource('sql/insert_sample.sql') as f:
        db_con.executescript(f.read().decode('utf8'))
