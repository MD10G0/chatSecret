#FrontEnd -  HTML, CSS & JAVA
#BackEnd - PYTHON
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Criar funcionalidade de enviar as mensagens
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, brodcast=True)

#criar 1 pagina = 1 rota 
@app.route("/") #decorator (atribui uma funcionalidade para função abaixo)
def homepage():
    return render_template("homepage.html")
     
#roda o nosso aplicativo
if __name__ == "__main__":
    socketio.run(app, host='localhost') 