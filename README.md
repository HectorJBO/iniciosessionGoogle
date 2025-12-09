# Proyecto Universitario: Inicios de Sesión Falsos (Phishing Educativo)

Este proyecto fue desarrollado con fines **exclusivamente educativos** . Su objetivo principal es **concientizar a las personas sobre el robo de información (phishing)** y demostrar cómo los atacantes pueden crear páginas falsas para engañar a los usuarios.

⚠️ **Advertencia importante:**  
Este proyecto **no debe usarse con fines maliciosos**. Todo uso debe mantenerse dentro de un entorno controlado, educativo y autorizado.

---

## 📌 Descripción del Proyecto
El repositorio contiene una página web con una ruleta que simula ser El Gallo mas Gallo una empresa en constante promocion.
Al obtener un premio la página web te incita a poner tus credenciales en un **login** diseñado para simular un inicio de sesión falso inspirado en proveedores conocidos(Google, Facebook).  
La finalidad es mostrar de forma práctica cómo las víctimas pueden ser engañadas al ingresar sus credenciales en sitios fraudulentos.

### Características del proyecto:
- Interfaz simple que simula un formulario de inicio de sesión.
- Uso de HTML, CSS, JavaScript y Flask.
- Botón de inicio de sesión con Facebook.
- Redirección generada con herramientas de pentesting.

### ⚠️ Sobre el botón de Facebook
El enlace utilizado en el botón de **“Iniciar sesión con Facebook”** fue generado usando **Zphisher** en **Kali Linux**, una herramienta usada en entornos de pruebas de seguridad.  
Ese enlace se incluye únicamente para **fines demostrativos** dentro del contexto académico.

---

## 🎯 Objetivo Académico
- Mostrar cómo operan las técnicas de phishing.  
- Demostrar los riesgos de ingresar datos en páginas no verificadas.  
- Fomentar buenas prácticas de ciberseguridad entre los usuarios.

---

## 📂 Estructura del proyecto
```
/Proyecto clases
 /iniciosessionGoogle
  │── static/css/styles.css/password.css/──scripts/infor.js/animation.js/──premios/──images
  │── templates/index.html/__inicio.html/__password.html
  │── datos.py 
  │── forms.py
  |__ premios.py
  |__ routes.py
  │── README.md
|__ star.py
|__ usuarios.json
|__ vercel.json
```
---

## 🛡️ Recomendaciones de Seguridad
- Verificar siempre la URL antes de ingresar credenciales.
- Activar la autenticación en dos pasos.
- No abrir enlaces sospechosos.
- Enseñar a otros sobre los riesgos del phishing.

---

## 🖥️ Tecnologías utilizadas
- HTML5
- CSS3
- JavaScript
- Python / Flask
- Herramientas de pentesting (Zphisher en Kali Linux)

---

## 📘 Uso del proyecto
1. Clona el repositorio:
```
git clone https://github.com/HectorJBO/iniciosessionGoogle.git
```
2. Ejecuta el proyecto en un entorno controlado.
3. Úsalo para una exposición, demostración o análisis de ciberseguridad.

---

## 🔒 Declaración de Responsabilidad
Este proyecto fue desarrollado **solo para fines educativos**.  
El autor y los colaboradores **no se responsabilizan por usos indebidos** fuera del contexto académico.

---
## 👨‍💻 Colaboradores
- **Denzel Moncada**
- **Noriam Pacheco**
- **Lesly pacheco**
- **jared Alvarez**

---
## 👨‍💻 Autor
**Héctor Betanco**  
Proyecto universitario de concientización sobre ciberseguridad.
