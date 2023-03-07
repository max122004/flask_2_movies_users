from дз18.dao.model.genres import Genres, GenresSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        return genres

    def get_one(self, mid):
        genres = Genres.query.get(mid)
        return genres
