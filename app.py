from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"

@app.route("/info")
def endpoint():

    datos=requests.get("https://api.chucknorris.io/jokes/random")
    datos=datos.json()
    print(datos)

    _str= "<p>Id: "+datos["id"]+"</p>" + "<p>URL del icono: "+datos["icon_url"] + "</p>" +"<p>Valor: "+datos["value"]+"</p>"

    return _str
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)

