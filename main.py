from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import os
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def index():
    dados = json.loads(request.data)
    altura = float(dados['altura'])
    peso = float(dados['peso'])
    print(altura, peso)
    msg = ""
    if not peso or not altura:
        return {"msg":"Altura ou peso vazio"}
    imc = float((peso) / (altura **2))
    calc_imc = str(f'{imc:.2f}')
    if imc < 18.5:
        msg = 'abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        msg = 'peso normal'
    elif imc >= 25 and imc <= 29.9:
        msg = 'sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        msg = 'obesidade grau I'
    elif imc >= 35 and imc <= 39.9:
        msg = 'obesidade grau II'
    else:
        msg = 'obesidade grau III'
    
    return {"imc:":calc_imc, "msg:":msg}

    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
