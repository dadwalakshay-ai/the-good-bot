from .db import DBCursor


class ORM:
    def __init__(self):
        self.cursor = DBCursor()

    def get_users(self):
        return [str(user_obj[0]) for user_obj in self.cursor.read_many("SELECT user_id FROM Users")]

    def get_scores(self):
        return self.cursor.read_many("SELECT user, COUNT(user) from Tasks WHERE status=1 GROUP BY user ORDER BY COUNT(user) DESC")

    def create_user(self, user_id):
        self.cursor.write(f"INSERT INTO Users(user_id) VALUES('{user_id}')")

        return user_id
    
    def create_task(self, user_id, description):
        task_id = self.cursor.write(f"INSERT INTO Tasks(user, description) VALUES('{user_id}', '{description}')")

        return task_id

    def update_task(self, task_id, status):
        self.cursor.write(f"UPDATE Tasks SET status={status} WHERE id={task_id}")

        return task_id
