from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Dados simulados para a API
items = [
    {"image": "1.png", "nome": "Item 1", "descricao": "Descrição do Item 1"},
    {"image": "1.png", "nome": "Item 2", "descricao": "Descrição do Item 2"},
    {"image": "1.png", "nome": "Item 3", "descricao": "Descrição do Item 3"},
    {"image": "1.png", "nome": "Item 4", "descricao": "Descrição do Item 4"},
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
