from flask import Flask, request, jsonify
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
	data= request.get_json()
	n1= data.get("n1")
	n2= data.get("n2")
	operation = data.get("operation")

	if not all([n1,n2,operation]):
		return "Erro: preencha os campos"

	try:
		n1,n2, = float(n1), float(n2)
	except ValueError:
		return "Erro: os valores nao sao numeros validos"

	match operation:
		case "/":
			result= n1/n2

		case "*":
			result= n1*n2
		
		case "+":
			result= n1+n2

		case "-":
			result = n1-n2
		
		case _:
			return("Erro: operaçao invalida")
	
	return jsonify({"n1": n1, "n2": n2, "operation": operation, "result": result})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

			