from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///WQT_May')
app =  Flask(__name__) 
api = Api(app)

class Question(Resource):
    def get(self):
        conn = db_connect.connect(
            #host = "127.0.0.1",#"localhost",
            user = "guest2",
            password = "guest",
        )
        query = conn.execute("show fields from tablename")
        return {query}#'fields':[i[0] for i in query.fetchall()]}

api.add_resource(Question, '/question')

# may need to address password issue
            #    dbname = "WQT_May",
            #    host = "localhost",
            #    user = "guest2",
            #   password = "guest",
            #    port = 5432

if __name__ == '__main__':
     app.run(port='5432')