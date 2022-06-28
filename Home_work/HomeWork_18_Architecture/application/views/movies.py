from flask import request, jsonify
from flask_restx import Resource, Namespace
from application.dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


"""Представления для сущности фильмы /movies/."""
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Метод для получения всех фильмов.
        Для получения фильма/ов за определенный год."""
        try:
            if movie_service.get_all():
                all_movies = movie_service.get_all()
                return movies_schema.dump(all_movies), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404

        year = request.args.get("year")
        try:
            if year:
                all_year_movie = movie_service.get_year_movie(year)
                return movies_schema.dump(all_year_movie), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404

    def post(self):
        """Метод для добавления фильма."""
        req_json = request.json
        movies_id = req_json["id"]  # Заголовок Location в POST на создание сущности.
        movie_service.create(req_json)
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = f'/{movies_id}'
        return response


"""Представления для сущности фильмы /movies/<int:mid>."""
@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        """Метод для получения одного фильма по его ID.
        Для получения фильма/ов с одним режиссером.
        Для получения фильма/ов с одним жанром."""
        try:
            director_id = request.args.get("director_id")
            if director_id:
                movie_dir = movie_service.get_directors_id(director_id)
                return movie_schema.dump(movie_dir), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404

        try:
            genre_id = request.args.get("genre_id")
            if genre_id:
                movie_genre = movie_service.get_genre_id(genre_id)
                return movie_schema.dump(movie_genre), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404

        try:
            if movie_service.get_one(mid):
                movie = movie_service.get_one(mid)
                return movie_schema.dump(movie), 200
        except Exception as not_found:
            return {"error": str(not_found)}, 404

    def put(self, mid: int):
        """Метод для изменения одного фильма по его ID."""
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        """Метод для частичного изменения одного фильма по его ID."""
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        """Метод для удаления одного фильма по его ID."""
        movie_service.delete(mid)

        return "", 204
