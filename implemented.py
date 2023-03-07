# файл для создания DAO и сервисов чтобы импортировать их везде
from setup_db import db
from дз18.dao.director import DirectorsDAO
from дз18.dao.genres import GenresDAO
from дз18.dao.movies import MoviesDAO
from дз18.dao.user import UsersDAO
from дз18.service.director import DirectorsService
from дз18.service.genres import GenresService
from дз18.service.movies import MoviesService
from дз18.service.user import UsersService

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao=movies_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao=genres_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao=directors_dao)

users_dao = UsersDAO(db.session)
users_service = UsersService(users_dao=users_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)