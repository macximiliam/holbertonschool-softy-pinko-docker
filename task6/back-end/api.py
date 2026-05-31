from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Escucha en todas las redes (0.0.0.0) y en el puerto 5252
    app.run(host='0.0.0.0', port=5252)
