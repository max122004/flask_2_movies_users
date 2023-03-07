from flask import request
from flask_restx import Resource, Namespace

from дз18.dao.model.user import UsersSchema
from дз18.implemented import users_service

user_ns = Namespace('users')

@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = users_service.get_all()
        result = UsersSchema(many=True).dump(users)
        return result, 200

    def post(self):
        req_json = request.json
        users_service.create_user(req_json)
        return '', 201