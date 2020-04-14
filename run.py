import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """ Add messages to list """
    messages.append(f"{username}: {message}")


def get_all_messages():
    """ Get all of the messages and seperate using br tag"""
    return "<br>".join(messages)


@app.route('/')
def index():
    """ Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """ Display chat usernames """
    return "<h1>Welcome, " + f"{username}</h1> {get_all_messages()}"


@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)