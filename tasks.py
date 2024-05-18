import random
from decouple import config

from db import ORM
from main import app


class Tasks:
    TASKS = [
        "Do 5 push-ups, STAT!",
        "Do some stretches, STAT!",
        "Drink a glass of water.",
        "Go talk to someone for a few minutes, You have been working hard for long.",
        "Chill and just take a stroll.",
    ]

    CHANNEL_ID = config("CHANNEL_ID")

    def __init__(self):
        self.query_handler = ORM()

        self.users = self.query_handler.get_users()

    def send_task(self):
        the_chosen_one = self.users[random.randint(0, (len(self.users) - 1))]

        the_chosen_task = self.get_random_task()

        task_id = self.query_handler.create_task(the_chosen_one, the_chosen_task)
        
        message = f"<@{the_chosen_one}>, {the_chosen_task}\nAre you done?"

        app.client.chat_postMessage(
            channel=self.CHANNEL_ID,
            text=message,
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"{message}"},
                    "accessory": {
                        "type": "radio_buttons",
                        "options": [
                            {
                                "value": f"{task_id}_1",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Yes"
                                }
                            },
                            {
                                "value": f"{task_id}_0",
                                "text": {
                                    "type": "plain_text",
                                    "text": "No"
                                }
                            },
                        ],
                        "action_id": "the-good-task-button",
                    }
                },
            ]
        )

    @classmethod
    def get_random_task(cls):
        return cls.TASKS[random.randint(0, (len(cls.TASKS) - 1))]


if __name__ == "__main__":
    task = Tasks()

    task.send_task()
