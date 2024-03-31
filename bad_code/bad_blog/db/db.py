import os
import sqlite3

import click
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_schema():
    db = get_db()
    schema = _read_sql_file("schema.sql")
    db.executescript(schema)


def init_data():
    db = get_db()
    data = _read_sql_file("data.sql")
    db.executescript(data)


@click.command("init-schema")
def init_schema_command():
    """Clear the existing data and create new tables."""
    init_schema()
    click.echo("Initialized the database.")


@click.command("init-data")
def init_data_command():
    """Insert new sample data into the database."""
    init_data()
    click.echo("Initialized data.")


def _read_sql_file(filename: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = f"sql/{filename}"
    with open(os.path.join(current_dir, relative_path)) as file:
        return file.read()
