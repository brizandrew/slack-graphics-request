# Graphics Request Slack App

This repo is for a session facilitated by me at SRCCON 2018 that goes by the same name. The project was meant to create a Slack app using as many as Slack's API functionalities as possible in order to showcase the full potential of using Slack as a front-end for newsroom tools. For notes on the session go to [SESSION.md](SESSION.md)

## Installation

Create a virtualenv to store the codebase.
```bash
$ virtualenv graphics-request
```

Activate the virtualenv.
```bash
$ cd graphics-request
$ . bin/activate
```

Clone the git repository from GitHub.
```bash
$ git clone https://github.com/brizandrew/slack-graphics-request repo
```

Enter the repo and install its dependencies.
```bash
$ cd repo
$ pip install -r requirements.txt
```

Fill out [`info.py`](app/info.py) with your Slack credentials.

Start the Flask app.
```bash
$ cd app
$ python app.py
```

## Routes
These are the routes that come with the Flask app and their intended uses:

### Index: `/`
Used to test that the app is running

### Events: `/events`
Used to handle all incoming requests about registered events being triggered.

### New Graphic: `/new-graphic`
Used to handle a slash command mapped to this route which will serve a dialog.

### Interactive Webhook: `/slack`
Used to handle all incoming interactive requests. This includes dialog submissions, interactive messages, and message actions.
