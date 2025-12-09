from flask import Flask

app = Flask(__name__)
app.secret_key = 'Messi10'


from app import routes


