import os
from flask import Flask, render_template, send_from_directory

# Create Flask app with static folder configuration
app = Flask(__name__, 
            static_url_path='/static',
            static_folder='static')
app.secret_key = os.environ.get("SESSION_SECRET", "dev-key-for-portfolio")

@app.route('/')
def index():
    return render_template('index.html')