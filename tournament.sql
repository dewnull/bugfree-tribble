-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE tournoments (id SERIAL PRIMARY KEY ,match_id) 
CREATE TABLE players (id SERIAL PRIMARY KEY, name as CHAR(150))
CREATE TABLE matches (id SERIAL PRIMARY KEY, player1 SERIAL , player2 SERIAL, winner SERIAL)