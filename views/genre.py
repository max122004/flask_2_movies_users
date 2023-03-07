from flask_restx import Resource, Namespace


from дз18.dao.model.genres import GenresSchema
from дз18.implemented import genres_service

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all()
        result = GenresSchema(many=True).dump(genres)
        return result, 200

@genres_ns.route('/<int:mid>')
class GenresView(Resource):
    def get(self, mid):
        genres = genres_service.get_one(mid)
        result = GenresSchema().dump(genres)
        return result, 200
