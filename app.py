from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from beans.myq import MySql
from beans.validator import Validator
import datetime

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*"}})

# ROTAS

@app.route("/") 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def home(): 
    return "API - V.1.0.0 "


@app.route("/login", methods=['POST']) 
@cross_origin(origin='http://localhost:4200',headers=['Content- Type','Authorization'])
def login(): 
    body = request.get_json()
    validator = Validator()
    
    if request.method == 'POST':
        try:
            m = MySql()
            user = validator.login(body['login'],body['senha'])
            if(bool(user)):
                return jsonify(user)
            return jsonify({"error":"Usuário não identificado!"})
            
        except Exception as e:
            print(e)
            return jsonify({"error": "Erro de login!"})
    else:
        return jsonify({"error": "Método não aceito!"}) 


@app.route("/steam", methods=['GET','POST','PUT']) 
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def steam(): 
    #recupera itens de json enviados por post
    body = request.get_json()
    #recupera a key hascode enviada por get
    hascode = request.args.get('hascode')
    
    # Verificação se o usuário está logado
    if(not Validator().checkHash(hascode)):
        return jsonify({"error": "Usuário sem permissão de acesso!"})
    
    # Implementação do método GET
    if request.method == 'GET':
        try:
            db = MySql()
            # SELECT na tabela de Sensor de vapor
            query = db.select('steam_sensor')
            return jsonify(query)
        except:
            jsonify({"error": "Erro de requisição!"})
            
    # Implementação do método POST
    elif request.method == 'POST':
        try:
            db = MySql()
            body['dtupdate'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            # INSERT retorna ID do item inserido na tabela sensor de vapor
            id = db.insert('steam_sensor', body)
            query = db.select('steam_sensor', where='id="%s"' % str(id))
            return jsonify(query)
        except:
            return jsonify({"error": "Erro de requisição!"})
    else:
        return jsonify({"error": 'Método não implementado!'})
    
#Rotina principal de execução do WS    
if __name__ == '__main__':
    app.run()