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

class MonNum(Resource):
    def get(self, mon_num):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where Mon =%d "  %int(mon_num))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class YearMon(Resource):
    def get(self, year_num):
        conn = db_connect.connect()
        query = conn.execute("select Mon from Aqueduct_Data where Year =%d" %int(year_num))
        #return {'month':[i[0] for i in query.fetchall()]}
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


class YearMonNum(Resource):
    def get(self, year_num, mon_num):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where Year =%d AND Mon =%d" %(int(year_num), int(mon_num)))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Var_Select(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Mon from Aqueduct_Data")
        return {'month':[i[0] for i in query.fetchall()]}

class Variable(Resource):
    def get(self, var):
        conn = db_connect.connect()
        query = conn.execute("select %s from Aqueduct_Data" %str(var))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class YearRange(Resource):
    def get(self, year_start, year_end):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where Year BETWEEN %d AND %d" %(int(year_start), int(year_end)))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class DateRange(Resource):
    def get(self, year_start, year_end, mon_start, mon_end):

        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where (Year > %d AND Year < %d) OR (Year = %d AND Mon >= %d) OR (Year = %d AND Mon <= %d)"
                             %( int(year_start), int(year_end), int(year_start), int(mon_start),int(year_end), int(mon_end)))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Test(Resource):
    def get(self): #, v1,v2):
        conn = db_connect.connect()
        query = conn.execute("select * from Aqueduct_Data where (Year > %d AND Year < %d) OR (Year = %d AND Mon >= %d) OR (Year = %d AND Mon <= %d)"
                             %( int(sd), int(ed), int(sd), int(mon_start),int(ed), int(em)))
        #"select Mon from Aqueduct_Data where Year = 1905")
            #"select * from Aqueduct_Data where (Year > 1905 AND Year < 1935) OR (Year = 1905 AND Mon >= 4) OR (Year = 1936 AND Mon <= 5)") #%(int(v1), int(v2)))
            #(sd, sm, ed, em, path)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)



api.add_resource(Years, '/year') 
api.add_resource(YearNum, '/year/<year_num>') 
api.add_resource(Id, '/id')
api.add_resource(Id_num, '/id/<id_num>')
api.add_resource(Month, '/month')
api.add_resource(MonNum, '/month/<mon_num>')
#api.add_resource(Variable, '/variable')
api.add_resource(Variable, '/<var>')


api.add_resource(YearMon, '/year/<year_num>/month')
api.add_resource(YearMonNum, '/year/<year_num>/month/<mon_num>')
api.add_resource(YearRange, '/year/<year_start>/<year_end>')
api.add_resource(DateRange, '/year/<year_start>/<year_end>/month/<mon_start>/<mon_end>')

api.add_resource(Test, '/test')#/<v1>/<v2>')



if __name__ == '__main__':
     app.run(port='5002')