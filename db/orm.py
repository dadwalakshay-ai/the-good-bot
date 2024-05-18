from .db import DBCursor


class ORM:
    def __init__(self):
        self.cursor = DBCursor()

    def get_users(self):
        return [str(user_obj[0]) for user_obj in self.cursor.read_many("SELECT user_id FROM Users")]
    
    def create_user(self, user_id):
        self.cursor.write(f"INSERT INTO Users(user_id) VALUES('{user_id}')")

        return user_id
