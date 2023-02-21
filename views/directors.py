from flask import request
from flask_restx import Resource, Namespace
from dao.models.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    def post(self):
        data = request.json
        director_service.create(data)
        return "", 201


@director_ns.route('/<int:d_id>')
class DirectorView(Resource):
    def get(self, d_id):
        director = director_service.get_one(d_id)
        return director_schema.dump(director), 200

    def put(self, d_id):
        data = request.json
        director_service.update(data, d_id)
        return "", 204

    def patch(self, d_id):
        data = request.json
        director_service.update_partial(data, d_id)
        return "", 204

    def delete(self, d_id):
        director_service.delete(d_id)
        return "", 204
