from info import sc_bot, SHARE_CHANNEL_ID


def alert_done(name, message_url):
    """
    Handle a new star being added to a message.
    """
    message = "This graphic, {}, is completed: {}".format(name, message_url)
    sc_bot.api_call(
        "chat.postMessage",
        channel=SHARE_CHANNEL_ID,
        text=message,
    )
