USE pokemonsearch;
select * from pokedex;
select * from pokemongo;
select pokedex.*, pokemongo.cp,pokemongo.defenserank,pokemongo.attackrank,pokemongo.healthrank from pokedex
LEFT JOIN pokemongo
ON pokedex.id = pokemongo.id;