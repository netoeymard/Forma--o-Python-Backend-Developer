import sqlite3
from pathlib import Path

from models.client import Client

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "database.db")
cur = con.cursor()
cur.row_factory = sqlite3.Row


def create_clients_table(cur: sqlite3.Cursor, con: sqlite3.Connection):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS clients \
            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
            nome VARCHAR(100), \
            email VARCHAR(100) \
            );"
    )
    con.commit()


def create_client(cur: sqlite3.Cursor, con: sqlite3.Connection, client: Client):
    cur.execute("INSERT INTO clients (nome, email) VALUES (?,?);", tuple(client))
    con.commit()


def update_client(
    cur: sqlite3.Cursor, con: sqlite3.Connection, client: Client, id: int
):

    cur.execute(
        "UPDATE clients SET nome = ?, email = ? WHERE id = ?",
        [client.nome, client.email, id],
    )
    con.commit()


def remove_client(cur: sqlite3.Cursor, con: sqlite3.Connection, id: int):
    cur.execute("DELETE from clients WHERE id = ?", [id])
    con.commit()

def list_client(cur: sqlite3.Cursor, con: sqlite3.Connection):
    results = cur.execute("SELECT * FROM clients").fetchall()

    for row in results:
        print(dict(row))

list_client(cur,con)

cur.close()
con.close()
