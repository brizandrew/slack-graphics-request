from info import sc_bot, REQUEST_CHANNEL_ID, REQUEST_TYPES


def request_made(payload):
    """
    Handle a new request being submitted.
    """
    # Parse payload
    username = payload["user"]["name"]
    user_id = payload["user"]["id"]
    channel_id = payload["channel"]["id"]
    submission = payload["submission"]

    # Create message
    text = "*\"{story}\"* {type} Request".format(
        story=submission["story"],
        type=REQUEST_TYPES[submission["type"]]
    )

    attachments = [
        {
            "author_name": username,
            "text": submission["description"],
            "fields": [
                {
                    "title": "Type",
                    "value": REQUEST_TYPES[submission["type"]],
                    "short": True
                },
                {
                    "title": "Story",
                    "value": submission["story"],
                    "short": True
                },
            ],
        },
        {
            "text": "Assigned To",
            "attachment_type": "default",
            "callback_id": "assignment_made",
            "actions": [{
                "name": "developers",
                "text": "Pick a developer...",
                "type": "select",
                "data_source": "users"
            }]
        }
    ]

    # Post message to channel and retrieve response
    resp = sc_bot.api_call(
        "chat.postMessage",
        channel=REQUEST_CHANNEL_ID,
        text=text,
        attachments=attachments
    )

    # Pin new requests
    message_ts = resp["message"]["ts"]
    sc_bot.api_call(
        "pins.add",
        channel=REQUEST_CHANNEL_ID,
        timestamp=message_ts
    )

    # Confirm to user that the request was made
    confirmation = "Your request for a *{type}* graphic for the story"
    confirmation += " *\"{story}\"* has been made."
    confirmation += " You can track its progress in <#{channel}>."
    confirmation = confirmation.format(
        type=REQUEST_TYPES[submission["type"]],
        story=submission["story"],
        channel=REQUEST_CHANNEL_ID
    )
    sc_bot.api_call(
        "chat.postEphemeral",
        text=confirmation,
        channel=channel_id,
        user=user_id
    )
