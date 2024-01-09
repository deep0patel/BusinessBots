from flask import Flask, jsonify, request
from http import HTTPStatus


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "password"
    return app


