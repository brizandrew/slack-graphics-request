from info import sc_bot, REQUEST_STATUSES


def assignment_made(payload):
    """
    Handle a new assignment made via the selection menu.
    """
    # Parse the payload
    selection = payload["actions"][0]["selected_options"][0]["value"]
    channel_id = payload["channel"]["id"]
    message_ts = payload["message_ts"]

    # Recreate original message
    message = payload["original_message"]
    text = message["text"]
    attachments = message["attachments"]

    # Update assignment selection
    attachments[1]["actions"][0]["selected_options"] = [
        {
            "text": "<@%s>" % selection,
            "value": "%s" % selection
        }
    ]

    # Add status dropdown if it's not there
    if (len(attachments) < 3):
        status_types = [{
            "value": key,
            "text": REQUEST_STATUSES[key]
        } for key in REQUEST_STATUSES.keys()]

        status_selection = {
            "title": "Status",
            "fallback": "Choose a status",
            "callback_id": "status_change",
            "actions": [{
                "name": "status",
                "text": "Set a status...",
                "type": "select",
                "options": status_types,
                "selected_options": [status_types[0]]
            }]
        }
        attachments.append(status_selection)

    # Update original message with changes
    sc_bot.api_call(
        "chat.update",
        channel=channel_id,
        ts=message_ts,
        text=text,
        attachments=attachments
    )
