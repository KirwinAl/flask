"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    @app.route("/index.html")
    def index():
        return render_template('index.html')

    @app.route("/aboutme.html")
    def aboutPage():
        return render_template('aboutme.html')

    @app.route("/gitPage.html")
    def gitPage():
        return render_template('gitPage.html')
    @app.route("/dockerPage.html")
    def dockerPage():
        return render_template('dockerPage.html')
    @app.route("/pythonPage.html")
    def pythonPage():
        return render_template('pythonPage.html')
    @app.route("/cicdPage.html")
    def cicdPage():
        return render_template('cicdPage.html')

    @app.route("/glossary.html")
    def glossaryPage():
        return render_template('glossary.html')
    @app.route("/aaatesting.html")
    def aaaPage():
        return render_template('aaatesting.html')
    @app.route("/oop.html")
    def oopPage():
        return render_template('oop.html')
    @app.route("/solid.html")
    def solidPage():
        return render_template('solid.html')

    return app
