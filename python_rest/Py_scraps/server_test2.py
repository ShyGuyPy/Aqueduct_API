from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


db_connect = create_engine('sqlite:///empty.db')
app =  Flask(__name__) 
api = Api(app)

class Reservoir_Intake_Test(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from TEST")#Reservoir_Intake")
        return {'Reservoir_Intake':[i[0] for i in query.fetchall()]}
        

class Year(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from Year")
        return {'Year':[i[0] for i in query.fetchall()]}

api.add_resource(Reservoir_Intake_Test, '/all') # Route_1
api.add_resource(Year, '/years') # Route_2



if __name__ == '__main__':
     app.run(port='5002')