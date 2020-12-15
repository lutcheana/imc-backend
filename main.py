from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    dados = json.loads(request.data)
    altura = float(dados['altura'])
    peso = float(dados['peso'])
    imc = float(peso / (altura **2))
    msg = ""
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

    

    

if __name__ == '__main__':
    app.run(debug=True)
