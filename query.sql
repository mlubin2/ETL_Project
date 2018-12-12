USE movie_search_db;
SELECT * FROM movies
inner JOIN oscar
ON movies.moviesearch = oscar.moviesearch;
