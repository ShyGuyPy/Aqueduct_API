from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///Aqueduct.db')
app =  Flask(__name__) 
api = Api(app)

class Years(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Year from Aqueduct_Data")
        return {'years':[i[0] for i in query.fetchall()]}



class YearNum(Resource):
    def get(self, year_num):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where Year =%d "  %int(year_num))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Id(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Id from Aqueduct_Data")
        return {'ids':[i[0] for i in query.fetchall()]}

class Id_num(Resource):
    def get(self, id_num):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where Id =%d "  %int(id_num))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Month(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Mon from Aqueduct_Data")
        return {'month':[i[0] for i in query.fetchall()]}

class Var_Select(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Mon from Aqueduct_Data")
        return {'month':[i[0] for i in query.fetchall()]}

class Variable(Resource):
    def get(self, var):
        conn = db_connect.connect()
        query = conn.execute("Select %s from Aqueduct_Data" %str(var))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Years, '/year') 
api.add_resource(YearNum, '/year/<year_num>') 
api.add_resource(Id, '/id')
api.add_resource(Id_num, '/id/<id_num>')
api.add_resource(Month, '/month') 
#api.add_resource(Variable, '/variable')
api.add_resource(Variable, '/<var>') 




if __name__ == '__main__':
     app.run(port='5002')