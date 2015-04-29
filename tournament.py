#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
	"""Connect to the PostgreSQL database.  Returns a database connection."""
	return psycopg2.connect("host='opensystems.crbp7d2xdj5m.us-east-1.rds.amazonaws.com' dbname='tournament' user='jharvard' password='crimson'")


def deleteMatches():
	"""Remove all the match records from the database."""
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM matches")
	DB.close()

def deletePlayers():
	"""Remove all the player records from the database."""
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM players")
	DB.close()

def countPlayers():
  """Returns the number of players currently registered."""
  DB = connect()
  c = DB.cursor()
  c.execute("SELECT COUNT(*) FROM players")
  result = c.fetchone()[0]
  DB.close()
  return result

def registerPlayer(name):
	"""Adds a player to the tournament database.
	
	The database assigns a unique serial id number for the player.  (This
	should be handled by your SQL database schema, not in your Python code.)

  Args:
  	name: the player's full name (need not be unique).
	"""
	new_name = bleach.clean(name)
	try:
		DB = connect()
  except:
    print "Unable to connect"
  try:
    c = DB.cursor()
		c.execute("INSERT INTO players (name) VALUES ('%s');" % (new_name,))
		c.commit()
		c.close()
	except:
		print "Unable to register player INSERT INTO players (name) VALUES ('%s')" % (new_name,)

def playerStandings():
	"""Returns a list of the players and their win records, sorted by wins.
	
	The first entry in the list should be the player in first place, or a player
	tied for first place if there is currently a tie.

	Returns:
		A list of tuples, each of which contains (id, name, wins, matches):
		id: the player's unique id (assigned by the database)
		name: the player's full name (as registered)
		wins: the number of matches the player has won
		matches: the number of matches the player has played
	"""
	result = []
	try:
		DB = connect()
		c = DB.cursor()
		c.execute("SELECT * FROM standing ORDER BY wins DESC, allmatches ASC")
		result = c.fetchall()
		c.close()
	except:
		print "Unable to register player"
		
	return result

def reportMatch(winner, loser):
	"""Records the outcome of a single match between two players.
	
	Args:
		winner:  the id number of the player who won
		loser:  the id number of the player who lost
	"""
	winner = bleach.clean(winner)
	loser  = bleach.clean(loser)
	try:
		DB = connect()
		c = DB.cursor()
		c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser))
		c.commit()
		c.close()
	except:
		print "Unable to report a Match"
 
def swissPairings():
	"""Returns a list of pairs of players for the next round of a match.
	
	Assuming that there are an even number of players registered, each player
	appears exactly once in the pairings.  Each player is paired with another
	player with an equal or nearly-equal win record, that is, a player adjacent
	to him or her in the standings.
	
	Returns:
	A list of tuples, each of which contains (id1, name1, id2, name2)
		id1: the first player's unique id
		name1: the first player's name
		id2: the second player's unique id
		name2: the second player's name
	"""
