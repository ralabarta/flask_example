from flask import Flask,request, url_for
from flask import render_template

app=Flask(__name__)

app.debug = True #Debug mode

#url_for('static',filename='style.css')

@app.errorhandler(404)
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='Post':
        return "Esto es un Post"
    else:
        return "Hello World! my friend-GET"

@app.route("/hello/")#Usando templates estaticos
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name = name)

@app.route("/otra")
def otra():
    return "Yo soy otra URL"

@app.route("/post/<int:post_id>")
def mostrar_port(post_id):
    return "Post %d" %post_id

@app.route("/user/<usuario>")
@app.route("/usuario/<usuario>")
def mostrar_perfil_usuario(usuario):
    return "Usuario %s" %usuario

if __name__ == "__main__":
    app.debug = True
    app.run()


