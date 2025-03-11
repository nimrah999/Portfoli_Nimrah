import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')
app.secret_key = os.environ.get("SESSION_SECRET", "dev-key-for-portfolio")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)
