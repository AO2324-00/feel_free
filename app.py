from flask import Flask, request
from flask_cors import CORS

from controllers import Place as P, Lend as L, Registration as Reg, Reserve as Res

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/places', methods = ["GET"])
def places():
    return P.get_places()

@app.route('/place/<id>', methods = ["GET"])
def place(id):
    return P.get_place(id)

@app.route('/lend/<id>', methods = ["GET"])
def lend(id):
    return L.get_lend(id)

@app.route('/registration', methods = ["POST"])
def registration():
    return Reg.registration(request)

@app.route('/reserve', methods = ["POST"])
def reserve():
    return Res.reserve(request)

if __name__ == '__main__':
    app.run()