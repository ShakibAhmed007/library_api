from flask_restplus import Api
from .library import api as ns1

api = Api(
    title='Test Api',
    version='1.0',
    description='Flask Rest Api Using Restplus'
)


api.add_namespace(ns1)