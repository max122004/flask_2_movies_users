from дз18.dao.model.director import Directors


class DirectorsDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = Directors.query.all()
        return directors

    def get_one(self, mid):
        directors = Directors.query.get(mid)
        return directors