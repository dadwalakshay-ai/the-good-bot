from decouple import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


app = App(token=config("SLACK_BOT_TOKEN"))


@app.event("member_joined_channel")
def greet(event, say):
    say(f"Welcome to the OG gang, <@{event['user']}>.")


@app.command("/iamshy")
def shy_announcement(ack, respond, command):
    ack(f"Thanks <@{command['user_id']}> for your announcement; we'll relay this anonymously.")

    announcement = f"""Someone anonymously announced...\n"{command['text']}" """

    app.client.chat_postMessage(channel=command['channel_id'], text=announcement)
    

if __name__ == "__main__":
    SocketModeHandler(app, config("SLACK_APP_TOKEN")).start()

