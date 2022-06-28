from flask_restx import Resource, Namespace
from application.dao.model.genres import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

"""Представление для сущности жанры /genres/."""
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Метод для получения всех жанров."""
        try:
            all_genres = genre_service.get_all()
            return genres_schema.dump(all_genres), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404


"""Представление для сущности жанры /genres/<int:gid>."""
@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """Метод для получения одного жанра по его ID."""
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404
