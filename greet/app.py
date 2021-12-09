# Put your app in here.
"""Greet Flask application."""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """

@app.route('/welcome')
def welcome():
  return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
  return "welcome home"

@app.route('/welcome/back')
def welcome_back():
  return "welcome back"
