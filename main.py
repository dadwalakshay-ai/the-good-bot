from decouple import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


app = App(token=config("SLACK_BOT_TOKEN"))


@app.event("member_joined_channel")
def greet(event, say):
    say(f"Welcome to the OG gang, <@{event['user']}>.")


@app.command("/praise")
def echo_msg(ack, respond, command):
    ack(f"Thanks <@{command['user_name']}> for your praises; we'll relay this message anonymously.")

    respond(f"{command['text']}")
    

if __name__ == "__main__":
    SocketModeHandler(app, config("SLACK_APP_TOKEN")).start()

