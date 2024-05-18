from decouple import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from db import ORM


app = App(token=config("SLACK_BOT_TOKEN"))


@app.event("member_joined_channel")
def greet(event, say):
    query_handler = ORM()

    query_handler.create_user(event["user"])

    say(f"Welcome to the OG gang, <@{event['user']}>\n<https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHpicmU5cHc5ZDBqOHU2NTRuNDc1OTBqeGxtMmlia2duYmZoYXZ3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.gif|_>")


@app.action("the-good-task-button")
def handle_some_action(ack, body, respond):
    ack()

    query_handler = ORM()

    task_id, status = body["actions"][0]["selected_option"]["value"].split("_")

    query_handler.update_task(task_id, status)

    if status == "1":
        respond(f"Thanks for completing your task <@{body['user']['id']}>.")
    

@app.command("/iamshy")
def shy_message(ack, command, say):
    ack(f"Thanks <@{command['user_id']}> for your message; we'll relay this anonymously.")

    announcement = f"""Someone anonymously said...\n"{command['text']}" """

    say(announcement)


@app.command("/score")
def scoreboard(ack, respond, command):
    ack()

    query_handler = ORM()

    scores = query_handler.get_scores()

    scoreboard = "Current scoreboard:\n"

    for score in scores:
        scoreboard += f"<@{score[0]}>: {score[1]}\n"

    respond(scoreboard)


if __name__ == "__main__":
    SocketModeHandler(app, config("SLACK_APP_TOKEN")).start()

