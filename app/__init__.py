from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'Messi10'

from app import routes


