import sqlite3
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

db = sqlite3.connect(BASE_DIR / "sqlite.db")
sql_insert = db.cursor()

def auth_user(first_name: str, last_name: str,
								password: str):
	sql_insert.execute(
		"""INSERT INTO users(
			first_name, last_name, password
		)VALUES(
			"%s", "%s", "%s"
		);""" % (first_name, last_name, password)
	)
	db.commit()

