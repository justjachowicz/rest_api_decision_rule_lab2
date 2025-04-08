from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Witaj w moim API'

@app.route('/mojastrona')
def mojastrona():
    return 'To jest moja strona!'

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', '')
    if name:
        return f"Hello {name}!"
    else: 
        return 'Hello!'

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    num1 = float(request.args.get('num1', ''))
    num2 = float(request.args.get('num2', ''))
    prediction = 0
    if num1 + num2 > 5.8:
        prediction = 1

    outputDict = {
        'prediction': prediction,
        'features': {
            'num1': num1,
            'num2': num2
        }
    }
    return outputDict
    

if __name__ == '__main__':
    app.run()
