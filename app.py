from flask import Flask
from flask_restx import Api

from дз18.config import Config
from дз18.setup_db import db
from дз18.views.movies import movies_ns
from дз18.views.director import directors_ns
from дз18.views.genre import genres_ns
from дз18.views.user import user_ns


# функция создания основного объекта app


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
