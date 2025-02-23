from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Configura CORS para aceitar todas as origens

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    n1 = data.get("n1")
    n2 = data.get("n2")
    operation = data.get("operation")

    if not all([n1, n2, operation]):
        return jsonify({"error": "Erro: preencha todos os campos"}), 400

    try:
        n1, n2 = float(n1), float(n2)
    except ValueError:
        return jsonify({"error": "Erro: os valores não são números válidos"}), 400

    match operation:
        case "/":
            if n2 == 0:
                return jsonify({"error": "Erro: divisão por zero"}), 400
            result = n1 / n2
        case "*":
            result = n1 * n2
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2
        case _:
            return jsonify({"error": "Erro: operação inválida"}), 400
    
    return jsonify({"n1": n1, "n2": n2, "operation": operation, "result": result})


# Tratamento para requisição OPTIONS (pre-flight) em CORS
@app.route('/calcular', methods=['OPTIONS'])
def options():
    return jsonify({}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
