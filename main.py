"""

  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
____________________________________
/ Si necesitas ayuda, contáctame en \
\ https://parzibyte.me               /
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Creado por Parzibyte (https://parzibyte.me).
------------------------------------------------------------------------------------------------
            | IMPORTANTE |
Si vas a borrar este encabezado, considera:
Seguirme: https://parzibyte.me/blog/sigueme/
Y compartir mi blog con tus amigos
También tengo canal de YouTube: https://www.youtube.com/channel/UCroP4BTWjfM0CkGB6AFUoBg?sub_confirmation=1
Twitter: https://twitter.com/parzibyte
Facebook: https://facebook.com/parzibyte.fanpage
Instagram: https://instagram.com/parzibyte
Hacer una donación vía PayPal: https://paypal.me/LuisCabreraBenito
------------------------------------------------------------------------------------------------
"""
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
"""
Clave secreta. Esta debe ser aleatoria, puedes generarla tú.
Primero instala Python y agrega python a la PATH: https://parzibyte.me/blog/2019/10/08/instalar-python-pip-64-bits-windows/
Luego abre una terminal y ejecuta:
python
Entrarás a la CLI de Python, ahí ejecuta:
import os; print(os.urandom(16));
Eso te dará algo como:
b'\x11\xad\xec\t\x99\x8f\xfa\x86\xe8A\xd9\x1a\xf6\x12Z\xf4'
Simplemente remplaza la clave que se ve a continuación con los bytes aleatorios que generaste
"""
app.secret_key = b'\xaa\xe4V}y~\x84G\xb5\x95\xa0\xe0\x96\xca\xa7\xe7'

"""
Definición de rutas
"""

# Protegida. Solo pueden entrar los que han iniciado sesión


@app.route("/escritorio")
def escritorio():
    return render_template("escritorio.html")

# Formulario para iniciar sesión


@app.route("/login")
def login():
    return render_template("login.html")

# Manejar login


@app.route("/hacer_login", methods=["POST"])
def hacer_login():
    correo = request.form["correo"]
    palabra_secreta = request.form["palabra_secreta"]
    # Aquí comparamos. Lo hago así de fácil por simplicidad
    # En la vida real debería ser con una base de datos y una contraseña hasheada
    if correo == "parzibyte@gmail.com" and palabra_secreta == "123":
        # Si coincide, iniciamos sesión y además redireccionamos
        session["usuario"] = correo
        # Aquí puedes colocar más datos. Por ejemplo
        # session["nivel"] = "administrador"
        return redirect("/escritorio")
    else:
        # Si NO coincide, lo regresamos
        flash("Correo o contraseña incorrectos")
        return redirect("/login")


# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


# Un "middleware" que se ejecuta antes de responder a cualquier ruta. Aquí verificamos si el usuario ha iniciado sesión
@app.before_request
def antes_de_cada_peticion():
    ruta = request.path
    # Si no ha iniciado sesión y no quiere ir a algo relacionado al login, lo redireccionamos al login
    if not 'usuario' in session and ruta != "/login" and ruta != "/hacer_login" and ruta != "/logout" and not ruta.startswith("/static"):
        flash("Inicia sesión para continuar")
        return redirect("/login")
    # Si ya ha iniciado, no hacemos nada, es decir lo dejamos pasar


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
