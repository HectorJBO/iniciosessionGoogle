from flask import Flask
from app import app as application  # importa tu aplicación interna

app = application  # Vercel necesita esta variable visible

if __name__ == "__main__":
    app.run(debug=True)
