import sqlite3

from . import auth

_conn = sqlite3.connect(":memory:", check_same_thread=False)
_conn.row_factory = sqlite3.Row
_conn.executescript(
    """
    CREATE TABLE users (username TEXT PRIMARY KEY, password_hash TEXT NOT NULL);
    CREATE TABLE assets (name TEXT PRIMARY KEY, status TEXT NOT NULL, location TEXT NOT NULL);
    INSERT INTO assets VALUES ('C-130J-01','FMC','Little Rock'),('C-130J-02','NMC','Ramstein'),('KC-46-07','PMC','McConnell');
    """
)
_conn.execute("INSERT INTO users VALUES (?, ?)", ("operator", auth.hash_password("Password1")))
_conn.commit()


def get_user(username: str):
    row = _conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    return dict(row) if row else None


def find_asset(name: str):
    # G4: SQL injection via string concatenation
    row = _conn.execute("SELECT * FROM assets WHERE name = '" + name + "'").fetchone()
    return dict(row) if row else None


def all_assets():
    return [dict(r) for r in _conn.execute("SELECT * FROM assets").fetchall()]
