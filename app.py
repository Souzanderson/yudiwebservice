from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from beans.myq import MySql
import datetime

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*"}})

# ROTAS

@app.route("/") 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def home(): 
    return "API - V.1.0.0 "

@app.route("/steam") 
@cross_origin(origin='*',headers=['Content- Type','Authorization'], methods = ['GET'])
def steam(): 
    m = MySql()
    m.select('steam_sensor')
    return jsonify(m)

#Rotina principal de execução do WS    
if __name__ == '__main__':
    app.run()