import sqlite3


class DBCursor:
    def __init__(self):
        self.conn = sqlite3.connect("db/the-good-bot.db")

        self.cursor = self.conn.cursor()

    def read(self, query):
        resp = self.cursor.execute(query)

        return resp.fetchone()

    def read_many(self, query):
        resp = self.cursor.execute(query)

        return resp.fetchall()

    def write(self, query):
        self.cursor.execute(query)

        self.conn.commit()
