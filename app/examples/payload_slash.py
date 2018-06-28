"""
If you're using the a generic flask route to handle your slash command
you'll receive a payload in the form of an ImmutableMultiDict found in the
request.form (remember you need to import request from flask in order to use
it). The pieces of this payload can be parsed out using the .get() method or by
[] selection. The key things to note are the "trigger_id" (which can be used to
trigger further interactions such as dialogs), "text" (which holds the text a
user inputed after the slash command), and "token" (which should be checked
against your records to confirm this command came from Slack).
"""

from collections import ImmutableMultiDict

slash_payload = ImmutableMultiDict([
    ('user_id', u'UBD84P929'),
    ('response_url', u'https://hooks.slack.com/commands/TBD0Y7WFM/389406301090/WQxxIPqMjhtmgnxRVXsRZU3L'),
    ('text', u''),
    ('token', u'ctc2l8oXd8i5ZjR7wijK8EGA'),
    ('trigger_id', u'388714401568.387032268531.c7cf79170e8159b40372d6db2737bccd'),
    ('channel_id', u'CBCSRDZ1S'),
    ('team_id', u'TBD0Y7WFM'),
    ('command', u'/graphic'),
    ('team_domain', u'srccon2018frontend'),
    ('user_name', u'briz.andrew'),
    ('channel_name', u'graphics-requests')
])

text = slash_payload.get("text")
