import json
from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from info import SLACK_VERIFICATION_TOKEN, REQUEST_CHANNEL_ID
from functions import (
    new_request,
    request_made,
    assignment_made,
    status_change,
    alert_done
)


app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(
    SLACK_VERIFICATION_TOKEN,
    "/events",
    app
)


def authorize(token):
    """
    Verfiy the message is coming from Slack
    """
    if token == SLACK_VERIFICATION_TOKEN:
        return True
    else:
        return False


@app.route("/", methods=["GET"])
def index():
    """
    Confirm that the server is working
    """
    return ("Working.")


@app.route("/new-graphic", methods=["POST"])
def new_graphic():
    """
    New graphic slash command webhook
    """
    # Authorize the request
    if not authorize(request.form["token"]):
        return (None, 403, None)

    # Parse the request
    trigger_id = request.form["trigger_id"]
    text = request.form["text"]

    # Handle the request
    new_request(trigger_id, text)

    return ("", 200)


@app.route("/slack", methods=["POST"])
def interactive_components():
    """
    Interactive components webhook
    """
    payload = json.loads(request.form["payload"])

    # Authorize the request
    if not authorize(payload["token"]):
        return (None, 403, None)

    # Handle dialog submissions
    if(payload["type"] == "dialog_submission"):
        if(payload["callback_id"] == "request_made"):
            request_made(payload)

    # Handle interactive messages
    elif(payload["type"] == "interactive_message"):
        if(payload["callback_id"] == "assignment_made"):
            assignment_made(payload)
        elif(payload["callback_id"] == "status_change"):
            status_change(payload)

    # Handle message actions
    elif(payload["type"] == "message_action"):
        if(payload["callback_id"] == "new_request"):
            trigger_id = payload["trigger_id"]
            text = payload["message"]["text"]
            new_request(trigger_id, text)

    return ("", 200)


@slack_events_adapter.on("star_added")
def event_starred(event):
    """
    Message had a star added to it event webhook.
    """
    item_starred = event.get("event").get("item")

    url = item_starred.get("message").get("permalink")
    text = item_starred.get("message").get("text")
    channel = item_starred.get("channel")

    if(channel == REQUEST_CHANNEL_ID):
        alert_done(text, url)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
