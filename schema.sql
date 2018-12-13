DROP database if exists pokemonsearch;
Create DATABASE pokemonsearch character set UTF8 collate utf8_bin;
USE pokemonsearch;



Create TABLE pokedex (
	id INT primary KEY,
	Name TEXT,
    Type_1 TEXT,
    Type_2 TEXT,
    Total INT,
    Generation INT,
    Legendary BOOLEAN) ;
    
CREATE TABLE pokemongo (
	id INT primary KEY,
    cp INT,
    defenserank INT,
    attackrank INT,
    healthrank INT);