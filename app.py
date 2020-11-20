from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

import datetime

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "http://localhost:4200"}})

# ROTAS

@app.route("/") 
@cross_origin(origin='http://localhost:4200',headers=['Content- Type','Authorization'])
def home(): 
    return "API - V.1.0.0 "
    
if __name__ == '__main__':
    app.run()