import mysql.connector
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template


app = Flask(__name__)

# set up routes
@app.route("/")
def dashboard():
        return render_template('index.html')

@app.route("/session")
def sessions():
        return render_template('session.html')

