from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! hola mundo saludos como estan'

@app.route('/Saludo')
def saluda():
    return 'Hola, Soy saludo'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    return 'El parametro es: {}'.format(param)

if __name__ == '__main__':
    app.run(debug=True, port=5000)