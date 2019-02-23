from flask import Flask, jsonify, request, json


app = Flask(__name__)
@app.route('/')
def index():
    return "hello world"