from flask import Blueprint
from flask_restful import Api
#from resources.Hello import Hello
#from resources.Category import CategoryResource
from resources.test_resource import The_Object
from resources.test_resource import Years
from resources.test_resource import CategoryResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#Route
api.add_resource(Years, '/year')
# api.add_resource(YearNum, '/year/<year_num>')
# api.add_resource(Id, '/id')
# api.add_resource(Id_num, '/id/<id_num>')
# api.add_resource(Month, '/month')
# api.add_resource(MonNum, '/month/<mon_num>')
# #api.add_resource(Variable, '/variable')
# api.add_resource(Variable, '/<var>')
#
#
# api.add_resource(YearMon, '/year/<year_num>/month')
# api.add_resource(YearMonNum, '/year/<year_num>/month/<mon_num>')
# api.add_resource(YearRange, '/year/<year_start>/<year_end>')
# api.add_resource(DateRange, '/year/<year_start>/<year_end>/month/<mon_start>/<mon_end>')
#
# api.add_resource(Test, '/test')

api.add_resource(The_Object, '/Hello')
api.add_resource(CategoryResource, '/Category')