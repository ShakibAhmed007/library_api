from flask_restplus import Resource,Namespace,fields,reqparse
from model.library_model import library_model
from flask import request

api = Namespace('library' , description='Library Api ')

"""
    for response marshalling
"""

library_models = api.model('Library',{"id":fields.Integer,
                                     "name":fields.String,
                                     "location":fields.String,
                                     "email":fields.String,
                                     "owner_name":fields.String,
                                     "owner_email":fields.String,
                                     "rating":fields.Integer
                                     })

""" 
    Resquest Parser
"""

parser = reqparse.RequestParser()
parser.add_argument('Library Body',  type=list, help='Library Data', location='json')

@api.route('/')
class library(Resource):
    @api.marshal_with(library_models,skip_none=True)
    def get(self):
        return library_model.get_all_library_list()

    @api.expect(parser)
    def post(self):
        library_data = request.get_json(force = True)
        return library_model.save_libarary_info(library_data)

    @api.expect(parser)
    def put(self):
        library_data = request.get_json(force = True)
        return library_model.update_library_info(library_data)


    @api.expect(parser)
    def delete(self):
        library_data = request.get_json(force=True)
        return library_model.delete_library_info(library_data)

