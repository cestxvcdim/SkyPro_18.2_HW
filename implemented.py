from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from services.director_service import DirectorService
from services.genre_service import GenreService
from services.movie_service import MovieService
from setup_db import db


director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
