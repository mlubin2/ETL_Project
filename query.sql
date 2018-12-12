USE movie_search_db;
SELECT * FROM movies;
SELECT * FROM oscar;
SELECT * FROM movies
INNER JOIN oscar
ON movies.Movie_Title = oscar.Film;