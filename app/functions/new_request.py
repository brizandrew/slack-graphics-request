from info import sc_bot, REQUEST_TYPES


def new_request(trigger_id, text=""):
    """
    Create and serve a new graphic dialog box.
    """
    # Create the options list
    types = [{
        "value": key,
        "label": REQUEST_TYPES[key]
    } for key in REQUEST_TYPES.keys()]

    # Create the form
    message = {
        "callback_id": "request_made",
        "title": "Request A Graphic",
        "submit_label": "Request",
        "elements": [
            {
                "type": "select",
                "label": "Type",
                "name": "type",
                "options": types
            },
            {
                "type": "text",
                "label": "Story",
                "name": "story",
                "placeholder": "What story is this graphic for?"
            },
            {
                "type": "textarea",
                "label": "Description",
                "name": "description",
                "placeholder": "Describe the graphic you envision.",
                "value": text
            }
        ]
    }

    # Open the dialog box
    sc_bot.api_call(
        "dialog.open",
        dialog=message,
        trigger_id=trigger_id
    )
