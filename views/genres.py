from flask import request
from flask_restx import Resource, Namespace
from dao.models.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:g_id>')
class GenreView(Resource):
    def get(self, g_id):
        genre = genre_service.get_one(g_id)
        return genre_schema.dump(genre), 200

    def put(self, g_id):
        data = request.json
        genre_service.update(data, g_id)
        return "", 204

    def patch(self, g_id):
        data = request.json
        genre_service.update_partial(data, g_id)
        return "", 204

    def delete(self, g_id):
        genre_service.delete(g_id)
        return "", 204
