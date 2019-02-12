from flask import Flask
from flask_restplus import Resource,Api
from resources.library import library
from resources import api

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
api.init_app(app)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug = True)