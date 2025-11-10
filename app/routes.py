from flask import render_template, redirect, url_for, request
from app import app

@app.route('/')
def home():
    return render_template('inicio.html')
    
