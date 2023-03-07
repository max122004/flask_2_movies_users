from flask_restx import Resource, Namespace

from дз18.dao.model.director import DirectorsSchema
from дз18.implemented import directors_service

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = get_all()
        result = DirectorsSchema(many=True).dump(directors)
        return result, 200

@directors_ns.route('/<int:mid>')
class DirectorsView(Resource):
    def get(self, mid):
        directors = directors_service.get_one(mid)
        result = DirectorsSchema().dump(directors)
        return result, 200