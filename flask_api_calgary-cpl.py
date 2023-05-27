# Flask API Template for Calgary-CPL Project

import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps("This is the Falsk API template for Calgary-CPL Project")
app.run()
