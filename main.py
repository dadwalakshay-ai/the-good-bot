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


@app.event("message")
def handle_message_events(body, logger):
    """Using this func to debug several User actions"""
    print(body)
    # import ipdb;ipdb.set_trace()


@app.command("/iamshy")
def shy_announcement(ack, respond, command):
    ack(f"Thanks <@{command['user_id']}> for your announcement; we'll relay this anonymously.")

    announcement = f"""Someone anonymously announced...\n"{command['text']}" """

    app.client.chat_postMessage(channel=command['channel_id'], text=announcement)
    

if __name__ == "__main__":
    SocketModeHandler(app, config("SLACK_APP_TOKEN")).start()

