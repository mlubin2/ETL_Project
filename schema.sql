DROP database if exists movie_search_db;
Create DATABASE movie_search_db character set UTF8 collate utf8_bin;
USE movie_search_db;



Create TABLE oscar (
	id INT auto_increment primary KEY,
	Ceremony INT,
    Film TEXT,
    Award_Count INT) ;
    
CREATE TABLE movies (
	id INT auto_increment primary KEY,
    Movie_Title TEXT,
    Year INT,
    Content_Rating TEXT,
    Budget_ADJ LONG,
    Gross_Income_ADJ LONG,
    Director TEXT,
    IMDB_Score INT);