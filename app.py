#!flask/bin/python
from flask import Flask, request
from flask_cors import CORS, cross_origin
from convert_numbers import convert

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def post():
    number = request.values["number"]
    print(number)
    if len(number) == 0:
        return ""

    data = convert(number.upper())
    if data is not None:
        return data
    return "Error"

if __name__ == '__main__':
    app.run()