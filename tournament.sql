-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE tournoments (id SERIAL PRIMARY KEY, match_id INTEGER); 
CREATE TABLE players (id SERIAL PRIMARY KEY, name as VARCHAR(150));
CREATE TABLE matches (id SERIAL PRIMARY KEY, 
					  player1 INTEGER, 
					  player2 INTEGER, 
					  winner INTEGER,
					  loser INTEGER,
					 FOREIGN KEY(winner) REFERENCES players(id),
					 FOREIGN KEY(loser) REFERENCES players(id) );
CREATE VIEW standing AS SELECT id, name (SELECT COUNT(*) FROM matches WHERE id = winner) AS wins,
(SELECT COUNT(*) FROM matches WHERE id IN (winner, loser)) AS matches FROM players GROUP BY id;