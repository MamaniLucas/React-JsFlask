from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
#inicializas flask
app = Flask(__name__)
CORS(app)

# Ruta de ejemplo para obtener todos los elementos


@app.route('/api/credit-cards', methods=['GET'])
def get_items():
    try:
        response = requests.get('https://api.placeholderjson.dev/credit-card')
        items = response.json()
        return jsonify(items), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Error al obtener los datos de la API pública'}), 500


# Ruta de ejemplo para crear un elemento


@app.route('/api/credit-cards/create', methods=['POST'])
def create_credit_card():
    data = request.get_json()

    # Validar los datos recibidos
    if 'type' not in data or 'number' not in data or 'expiry' not in data or 'cvc' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400

    # Crear un nuevo elemento
    new_item = {
        'type': data['type'],
        'number': data['number'],
        'expiry': data['expiry'],
        'cvc': data['cvc']
    }

    try:
        # Realizar la solicitud POST a la API externa
        response = requests.post('http://127.0.0.1:5000/api/credit-cards/', json=new_item)
        # Lanza una excepción si la respuesta tiene un código de error HTTP
        response.raise_for_status()

        # Devolver la respuesta de la API externa como JSON al cliente
        return jsonify(response.json()), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)
