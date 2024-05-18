from db import DBCursor


def migrate():
    cursor = DBCursor()

    cursor.cursor.execute("CREATE TABLE Users(id INTEGER PRIMARY KEY ASC, user_id VARCHAR UNIQUE NOT NULL)")
    cursor.cursor.execute("CREATE TABLE Tasks(id INTEGER PRIMARY KEY ASC, user INTEGER NOT NULL, status INTEGER DEFAULT 0, description VARCHAR, FOREIGN KEY(user) REFERENCES Users(id))")

    cursor.conn.commit()


if __name__ == "__main__":
   migrate()
