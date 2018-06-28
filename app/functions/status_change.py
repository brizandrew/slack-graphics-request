from info import sc_bot, REQUEST_STATUSES, REQUEST_CHANNEL_ID


def status_change(payload):
    """
    Handle a new status change made via the selection menu.
    """
    selection = payload["actions"][0]["selected_options"][0]["value"]

    channel_id = payload["channel"]["id"]
    message_ts = payload["message_ts"]

    message = payload["original_message"]
    text = message["text"]
    attachments = message["attachments"]

    # Update assignment selection
    attachments[2]["actions"][0]["selected_options"] = [
        {
            "text": REQUEST_STATUSES[selection],
            "value": selection
        }
    ]

    sc_bot.api_call(
        "chat.update",
        channel=channel_id,
        ts=message_ts,
        text=text,
        attachments=attachments
    )

    # Create a log of assignments
    assignment_log = "{user} changed the status to {status}".format(
        user=payload["user"]["name"],
        status=REQUEST_STATUSES[selection]
    )
    sc_bot.api_call(
        "chat.postMessage",
        channel=channel_id,
        thread_ts=message_ts,
        text=assignment_log,
    )

    # Pin/Unpin depending on status
    if(selection == "finished"):
        sc_bot.api_call(
            "pins.remove",
            channel=REQUEST_CHANNEL_ID,
            timestamp=message_ts
        )
    else:
        sc_bot.api_call(
            "pins.add",
            channel=REQUEST_CHANNEL_ID,
            timestamp=message_ts
        )
