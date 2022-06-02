import sqlite3
from collections import Counter


class DbConnect:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


def movie_by_title(title):
    db_connect = DbConnect("netflix.db")
    db_connect.cur.execute(f"""
                    SELECT title, country, release_year, listed_in, `description`
                    FROM netflix
                    WHERE title LIKE '%{title}%' ORDER BY release_year DESC LIMIT 1
    """)

    result = db_connect.cur.fetchone()
    return {
        "title": result[0],
        "country": result[1],
        "release_year": result[2],
        "genre": result[3],
        "description": result[4]
    }


def movies_by_years(year1, year2):
    db_connect = DbConnect("netflix.db")
    query = f"SELECT title, release_year, FROM netflix WHERE release_year BETWEEN '%{year1}%' AND '%{year2}%' LIMIT 100"
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    result_list = []
    for movie in result:
        result_list.append({"title": movie[0],
                            "release_year": movie[1]})

    return result_list


def movies_by_rating(rating):
    db_connect = DbConnect("netflix.db")
    rating_parameters = {
        "children": "'G'",
        "family": "'G', 'PG', 'PG-13'",
        "adult": "'R', 'NC-17'",
    }
    if rating not in rating_parameters:
        return "Переданной групы не существует"

    query = f"SELECT title, rating, `description` FROM netflix WHERE rating IN ({rating_parameters[rating]})"
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    result_list = []

    for rating in result:
        result_list.append({
            "title": rating[0],
            "rating": rating[1],
            "description": rating[2]
        }, )
    return result_list


def movies_by_genre(genre):
    db_connect = DbConnect("netflix.db")
    query = f"""
          SELECT title, `description`
          FROM netflix
          WHERE listed_in LIKE '%{genre}%'
          ORDER BY release_year DESC
          LIMIT 10
    """
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    result_list = []
    for movie in result:
        result_list.append({
            "title": movie[0],
            "description": movie[1]
        })
        return result_list


def cast_partners(actor1, actor2):
    db_connect = DbConnect("netflix.db")
    query = f"""
            SELECT `cast`
            FROM netflix
            WHERE `cast` LIKE '%{actor1}%' AND `cast` LIKE '%{actor2}%'
            """
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    actor_list = []

    for cast in result:
        actor_list.extend(cast[0].split(', '))
    counter = Counter(actor_list)
    result_list = []
    for actor, count in counter.items():
        if actor not in [actor1, actor2] and count > 2:
            result_list.append(actor)
    return result_list


def search_movie_by_param(movie_type, release_year, genre):
    db_connect = DbConnect("netflix.db")
    query = f"""
        SELECT title, `description`
        FROM netflix
        WHERE `type` = '{movie_type}'
        AND release_year = '{release_year}'
        AND listed_in LIKE '%{genre}%'
    """
    db_connect.cur.execute(query)
    result = db_connect.cur.fetchall()
    result_list = []
    for movie in result:
        result_list.append({'title': movie[0], 'description': movie[1]})
    return result_list

print(search_movie_by_param('TV Show', 2005, 'Drama'))
