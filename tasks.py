import random

from db import ORM
from main import app


class Tasks:
    TASKS = [
        "Do 5 push-ups, STAT!",
        "Go stretch your body.",
        "Drink a glass of water.",
        "Go talk to someone for a few minutes, You have been working so hard.",
        "Chill and just take a stroll.",
    ]

    CHANNEL_ID = "C0743JKAEAY"

    def __init__(self):
        query_handler = ORM()

        self.users = query_handler.get_users()

    def send_task(self):
        the_chosen_one = self.users[random.randint(0, (len(self.users) - 1))]

        the_chosen_task = self.get_random_task()

        message = f"<@{the_chosen_one}>, {the_chosen_task}"

        app.client.chat_postMessage(channel=self.CHANNEL_ID, text=message)

    @classmethod
    def get_random_task(cls):
        return cls.TASKS[random.randint(0, (len(cls.TASKS) - 1))]


if __name__ == "__main__":
    task = Tasks()

    task.send_task()
