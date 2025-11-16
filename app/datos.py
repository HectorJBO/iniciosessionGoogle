import json
import os 

archivo = "usuarios.json"

if not os.path.exists(archivo):
    with open(dict, "w") as f:
        json.dump([],f)


def agregar_usuario(email, password):
    with open(archivo, "r") as f:
        usuarios = json.load(f)
    nuevo = {"email": email, "password": password}
    usuarios.append(nuevo)

    with open(archivo, 'w') as f:
        json.dump(usuarios, f, indent=4)



