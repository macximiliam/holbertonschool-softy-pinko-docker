from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Escucha en todas las redes (0.0.0.0) y en el puerto 5252
    app.run(host='0.0.0.0', port=5252)
