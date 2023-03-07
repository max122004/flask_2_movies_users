from дз18.dao.genres import GenresDAO

class GenresService:
    def __init__(self, genres_dao):
        self.genres_dao = genres_dao

    def get_all(self):
        return self.genres_dao.get_all()

    def get_one(self, mid):
        return self.genres_dao.get_one(mid)