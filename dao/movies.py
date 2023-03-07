from дз18.dao.model.movies import Movies, MoviesSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        return movies

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        return movie

    def get_by_year(self, year):
        movie = Movies.query.filter(Movies.year == year)
        return movie

    def get_by_genre(self, genre_id):
        movie = Movies.query.filter(Movies.genre_id == genre_id)
        return movie

    def get_by_year(self, director_id):
        movie = Movies.query.filter(Movies.director_id == director_id)
        return movie

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
        self.session.close()