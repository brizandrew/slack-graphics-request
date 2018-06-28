"""
If you're using the a generic flask route to handle your slash command
you'll receive a payload in the form of an ImmutableMultiDict found in the
request.form (remember you need to import request from flask in order to use
it). This information however is locked inside a serialized JSON payload found
at the key of "payload". It must first be deserialized before it can be further
parsed by using the .get() method or by [] selection

The key things to note are the "trigger_id" (which can be used to
trigger further interactions such as dialogs), "message" (which contains all
the information about the message the action was called on), and "callback_id"
(which will tell you what action was selected).
"""

from collections import ImmutableMultiDict

action_payload = ImmutableMultiDict([
    ('payload', u'{
        "type": "message_action",
        "token": "ctc2l8oXd8i5ZjR7wijK8EGA",
        "action_ts": "1530160135.297737",
        "team": {
            "id": "TBD0Y7WFM",
            "domain": "srccon2018frontend"
        },
        "user": {
            "id": "UBD84P929",
            "name": "briz.andrew"
        },
        "channel": {
            "id": "CBCSRDZ1S",
            "name": "graphics-requests"
        },
        "callback_id": "new_request",
        "trigger_id": "389311462867.387032268531.59b0987b515cedbf0c603b63925c804b",
        "message_ts": "1529893861.000149",
        "message": {
            "type": "message",
            "user": "UBD84P929",
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "client_msg_id": "802cc536-5407-40ea-8b4d-da0e7e757f9a",
            "ts": "1529893861.000149"
        },
        "response_url": "https:\\/\\/hooks.slack.com\\/app\\/TBD0Y7WFM\\/389311462947\\/RLrTcJX8va6NbVNzjASujBg2"
        }'
    )
])

text = slash_payload.get("text")
