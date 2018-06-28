from slackclient import SlackClient
from collections import OrderedDict

# SENSITIVE INFO THAT SHOULD NOT LIVE HERE
SLACK_BOT_TOKEN = ''
SLACK_VERIFICATION_TOKEN = ''
# /END

REQUEST_CHANNEL_ID = 'CBCSRDZ1S'
SHARE_CHANNEL_ID = 'CBE5DKK9D'

REQUEST_TYPES = OrderedDict([
    ("map", "Map"),
    ("graph", "Graph"),
    ("flowchart", "Flowchart"),
    ("other", "Other")
])

REQUEST_STATUSES = OrderedDict([
    ("holding", "On Hold"),
    ("working", "Working"),
    ("editing", "Editing"),
    ("finished", "Finished")
])

sc_bot = SlackClient(SLACK_BOT_TOKEN)
