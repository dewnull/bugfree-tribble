-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE tournaments (id SERIAL PRIMARY KEY, match_id INTEGER); 
CREATE TABLE players (id SERIAL PRIMARY KEY, name VARCHAR);
CREATE TABLE matches (id SERIAL PRIMARY KEY, 
					  winner INTEGER,
					  loser INTEGER,
					 FOREIGN KEY(winner) REFERENCES players(id),
					 FOREIGN KEY(loser) REFERENCES players(id) );
CREATE VIEW standing AS 
	SELECT id,
		 name, 
		 (SELECT COUNT(*) FROM matches 
		  	WHERE players.id = matches.winner) AS wins,
		 (SELECT COUNT(*) FROM matches 
		  	WHERE players.id IN (matches.winner, matches.loser)) AS total_matches 
	FROM players
	GROUP by id;