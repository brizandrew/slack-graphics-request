"""
If you're using the events handler api library, the paylod will come in
through the first argument of that function. Items can be parsed using
the .get() method. In this example, we're using the star_added event which
dicates what we see in the "event" key. For a full list of events and their
event data check out: https://api.slack.com/events/api
"""

starred_payload = {
    u'event_time': 1530156763,
    u'api_app_id': u'ABCD1LRTJ',
    u'event_id': u'EvBGD4SQR5',
    u'authed_users': [u'UBD84P929'],
    u'team_id': u'TBD0Y7WFM',
    u'token': u'ctc2l8oXd8i5ZjR7wijK8EGA',
    u'type': u'event_callback',
    u'event': {
        u'event_ts': u'1530156763.000085',
        u'item': {
            u'date_create': 1530156763,
            u'message': {
                u'client_msg_id': u'a1350be5-6eb4-4ad2-885b-d2483c8215e3',
                u'permalink': u'https://srccon2018frontend.slack.com/archives/CBE5DKK9D/p1530156755000002',
                u'text': u'This message will be starred.',
                u'ts': u'1530156755.000002',
                u'user': u'UBD84P929',
                u'is_starred': True,
                u'type': u'message'
            },
            u'type': u'message',
            u'channel': u'CBE5DKK9D'
        },
        u'type': u'star_added',
        u'user': u'UBD84P929'
    }
}

message_starred = starred_payload.get("event").get("item").get("message")
message_starred_ts = message_starred.get("ts")
