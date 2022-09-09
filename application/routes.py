from flask import current_app as app
from flask_restx import Api, Namespace, Resource

from application.models import db
from application import models, schema

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')

movies_schema = schema.Movie(many=True)


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies = db.session.query(models.Movie).all()
        return movies_schema.dump(movies), 200
