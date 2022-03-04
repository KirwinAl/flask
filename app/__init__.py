"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def index():
        return render_template('index.html')
    @app.route("/index.html")
    def index2():
        return render_template('index.html')
    @app.route("/gitPage.html")
    def gitPage():
        return render_template('gitPage.html')
    @app.route("/dockerPage.html")
    def gitPage():
        return render_template('dockerPage.html')
    @app.route("/pythonPage.html")
    def gitPage():
        return render_template('pythonPage.html')
    @app.route("/cicdPage.html")
    def gitPage():
        return render_template('cicdPage.html')

    return app
