# Python - 2022 Summer Course
# Day 7
# Topic: SQL and Database
# Instructor: Annamaria Prati
# Former Instructors: Ben Noble, Patrick Cunha Silva, Ryden Buttler,
#             Erin Rossiter, Michele Torres
#             David Carlson, and Betul Demirkaya
# First Instructor: Matt Dickenson

import os
os.chdir('C:\\Users\\miame\\Documents\\GitHub\\python_summer2022\\Day7\\Lecture')

# What is a Database?
#   - A database is a collection of information that is organized so 
#     that it can be easily accessed, managed, and updated.
#   - In a relational database, digital information about a 
#     specific customer is organized into rows, columns, and 
#     tables which are indexed to make it easier to find relevant 
#     information through SQL queries.
# Source: https://searchsqlserver.techtarget.com/definition/database

# Why create a relational database
#   - Flexible, can add new data and new relationships easily
#   - Eliminates redundancies (e.g., a csv with several rows of repeated data)
# Source: https://www.ibm.com/cloud/learn/relational-databases

# Example:
# https://bit.ly/3iYBfkS

# We can use Python to manage databases
# We will focus on SQL (also pronounced sequel) databases
# We need to install sqlite first 

#---------- Installing sqlite ----------#

# install sqlite from sqlite.org:

# - On MAC, open terminal, then copy and paste:
#   brew install sqlite3

# - On Windows, follow this tutorial:
#   https://www.guru99.com/download-install-sqlite.html

#---------- Using sql with Python ----------#

# pip install sqlalchemy

# Check: http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
# To find documentation: https://www.kite.com/python/docs/

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_, distinct
from sqlalchemy.orm import relationship, backref, sessionmaker

# - Connect to the local database
# - The return value of create_engine() is an instance of Engine,
#   and it represents the core interface to the database
# - It is how SQLAlchemy communicates with our database.
# - We could use it to talk to the database directly,
#   but we'd rather use a Session object to work with
#   object relational mapping (ORM)

engine = sqlalchemy.create_engine('sqlite:///players.db', echo=True)

# The attribute echo=True will make SQLAlchemy log all SQL
# commands it is doing while you apply commands.
# The database will be intact, until you execute the commands


# - ORM: object relational mapping (https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
# - No need to write raw SQL! Instead interact with SQL using Python language.
# - It converts data between incompatible type systems
# - Uses class-like syntax to do three things at once:
#     1. describe database table
#     2. define our own python class object
#     3. "mapper" to map the python object to SQL table
# - All done together using Declarative system
# - In other words, creates classes that include directives
#   to describe the actual database table they will be mapped to
# - Classes mapped using the Declarative system are 
#   defined in terms of a Base class
# - Base class maintains a catalog of classes and tables 
#   relative to that base
# More information: https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one

# Instantiate a Base
Base = declarative_base() 

# Each class is a table in our db
# Each attribute will be a column in the table

# Define some schemas (The blueprint)

# One to Many example: basketball teams with many players
# - Two tables: one for players and one for teams
# - Foreign key on child (player) references unique team ID (the primary key)
# - relationship() method then specified by parent (team) to reference many items

# Our Player table has 4 columns: ID, Name, Number, and Team ID
class Player(Base):
  __tablename__ = 'players'

  ## At first, only specify data types for the columns
  ## primary_key is unique, non-nullable identifier for row
  ## Have an ID column because player attributes (name, etc) are not unique
  ## At least 1 primary_key per table
  id = Column(Integer, primary_key = True) 
  name = Column(String)
  number = Column(Integer)
  
  ## ForeignKey tells us we have a relationship with another table ("teams") by the ("id") variable
  ## This info constrained to only come from that table
  ## What we are referencing is usually the primary key for that table
  team_id = Column(Integer, ForeignKey("teams.id")) 

  ## Populate non-ID fields in the table through the constructor
  def __init__(self, name, number, team=None):
    self.name = name
    self.number = number
    self.team = team
    
  def __repr__(self):
    return "<Player('%s', '%s')>" % (self.name, self.number)

# Our Team table has 2 columns: ID and Name
class Team(Base):
  __tablename__ = "teams"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)

  ## - relationship() tells us another table wants to reference us
  ## - now notice we use "Player" object syntax and "team" member variable syntax
  ## - Note: this is NOT a column
  ##          but we can call <team obj>.players
  ##          or <player obj>.team
  players = relationship("Player", backref="team")
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "<team('%s')>" % (self.name)
    
# - First time create tables
# - The MetaData is a registry which includes the ability make schema commands
#    to database.
# - Our SQLite database does not actually have a players table present, 
#   so we use MetaData to issue the SQL "CREATE TABLE" command to the database
#   for all tables that don’t yet exist.

Base.metadata.create_all(engine) 

# - SQLAlchemy represents info for specific table with Table object
# So what columns do we have?
Player.__table__  
Team.__table__

# Very similar syntax to what we've done before with class definitions!
# One instance for each table
p1 = Player(name = "Joey", number = 27)
t1 = Team(name = "WashU")
# add team reference to player 
p1.team = t1
# now a part of team object
t1.players
p1.team

# Again...
# - Create a player
# - Just like we do with Python objects
mason = Player("Mason Plumlee", 5)
# Let's print the ID
print(mason.id)

# - Nothing?
# - Even though we didn’t specify it in the constructor, 
#   the id attribute still produces a value
#   of None when we access it (as opposed to Python’s usual 
#   behavior of raising AttributeError 
#   for an undefined attribute).
# - When we put the mason object in the db a real ID will be assigned

# - Create a session to actually store things in the db
# - The ORM’s "way into" to the database is the Session, a "holding zone" for
#   all the objects and associations we have created. The Session will hold
#   objects/associations until we commit or close

Session = sessionmaker(bind = engine)
session = Session()

# add player
session.add(mason)
session.add(p1)

# add multiple players
session.add_all([Player("Miles Plumlee", 40),
  Player("Seth Curry", 30), Player("LeBron James", 6),
  Player("The other Plumlee", 100), Player('KD', 7)])

# see what we've done this session
session.new 

# before we commit, if we made a mistake, we can correct it
# session.rollback()

# now make changes to actual db
session.commit()

# Test again for ID... 
# (it keeps the count in the order they entered the database)
print('ID: ' + str(mason.id))
print('ID: ' + str(p1.id))

# Some querying
# order the results
# you can think of it as... session.query(TABLE).order_by(COLUMN)
for player in session.query(Player).order_by(Player.number):
  print(player.number, player.name, player.id)
  
# limit the results
# 1. orders by number
# 2. grab by index
for player in session.query(Player).order_by(Player.id)[0:3]:
  print(player.number, player.name, player.id)

# Some filters
# lots of options: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators
for player in session.query(Player).filter(Player.name == "Mason Plumlee").order_by(Player.number):
  print(player.number, player.name)
  
for player in session.query(Player).filter(Player.name != "Mason Plumlee").order_by(Player.number):
  print(player.number, player.name)

# or_()
for player in session.query(Player).filter(or_(Player.name == "Mason Plumlee", Player.name == "Miles Plumlee")).order_by(Player.number):
  print(player.number, player.name)
  
# .like()
# return all the rows with 'name' column contains the partial string "Plum"
for player in session.query(Player).filter(Player.name.like("%Plum%")).order_by(Player.number):
  print(player.number, player.name)

# and_()
for player in session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number):
  print(player.number, player.name)

# functions
# we can also apply functions using the func package
from sqlalchemy import func

# note that I need to query the columns I want back
for player in session.query(Player.name, Player.number, func.max(Player.number)):
  print(player.name, player.number)


# Results can be indexed as lists
results = session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number)
results.first()
results[0]
results[1]

# Check the number of elements in results
results.count()

# Now to relations
# Player and Team tables
duke = Team('Duke')

# query all players
players = session.query(Player).all()
# Two ways to assign players to a team:
mason.team = duke
players[2].team = duke

# Check Duke's players
duke.players
# Check mason's team
mason.team

# We can get the roster from mason's team
mason.team.players

# Now note the id:
session.commit()
mason.team_id

# Lets load the two things together
# query(TABLE1, TABLE2)
for player, team in session.query(Player, Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print(player.number, player.name, team.name)

# or,
# query(TABLE1).join(TABLE2)
for i in session.query(Player).join(Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print(i.number, i.name, i.team.name)

# we can join and execute functions using subquery, e.g. the highest number by team
sub = session.query(func.max(Player.number).label('max')).join(Team).group_by(Team.name).subquery()

for player in session.query(Player).join(Team).filter(sub.c.max == Player.number):
  print(player.name, player.number, player.team.name)

# now deletion
# list we queried above
players
session.query(Player).filter(Player.number == 30).count()

# query 1 player
# now we have the representation of him
seth = session.query(Player).filter(Player.number == 30).first()

# now we can delete him
session.delete(seth)

# he's gone!
session.query(Player).filter(Player.number == 30).count()
session.query(Player).filter(Player.name.like("%Seth%")).count()

# But he is still in our object players
players
players = session.query(Player).all()
players 


# Updating
other_plumlee = players[4]
other_plumlee.name = "Marshall Plumlee"

# The Session is paying attention!
session.dirty
# Instances are considered dirty when they were modified but not deleted

# commit our changes
session.commit()
session.dirty


# print IDs 
[p.id for p in players]


# Add Annamaria
annamaria = Player(name = "Annamaria", number = 9)
session.add(annamaria)

session.commit()

# How to convert data to csv
players = session.query(Player).all()
for player in players:
  ## apply skills we've learned already
  print(player.name, player.number, player.team, player.id)

# Example:
import csv
with open("players.csv", 'w') as f:
    my_writer = csv.DictWriter(f, fieldnames = ("name", "number", "team"))
    my_writer.writeheader()
    for player in players:
        try:
            my_writer.writerow({"name":player.name, "number":player.number, "team":player.team.name})
        except AttributeError:
            my_writer.writerow({"name":player.name, "number":player.number, "team":""})

#---------- Another Example: Books ----------#

# book_table
#  title                  author_id   main_character        year
#  "War and Peace"        1           "Pierre Bezukhov"     1869
#  "Anna Karenina"        1           "Anna Karenina"       1877
#  "Tale of Two Cities"   2           "Alexandre Manette"   1859
#  "Crime and Punishment" 3           "Raskolnikov"         1866
 
# author_table
#  author_id       author_name     country_id
#  1               Tolstoy         1
#  2               Dickens         2
#  3               Dostoevsky      1
#  4               Darwin          1
 
# country_table
#  country_id        country_name      capital
#  1                 Russia            Moscow
#  2                 England           London


# Connect to the local database
engine = sqlalchemy.create_engine('sqlite:///books.db', echo=True)

# Declare Base
Base = declarative_base() 

# Define some schemas
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    main_character = Column(String)
    year = Column(Integer)
    ## how will this table speak to other tables?
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    def __init__(self, name, main_character=None, year=None):
      self.name = name
      self.main_character = main_character
      self.year = year
      
    def __repr__(self):
      if self.author: return "<Book(%s by %s)>" % (self.name, self.author.name)
      return "<Book(%s)>" %(self.name)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ## what does this do?
    country_id = Column(Integer, ForeignKey('countries.id'))

    ## what does this do?
    books = relationship('Book', backref='author')

    def __init__(self, name):
      self.name = name
    
    def __repr__(self):
      return "<Author('%s')>" % (self.name)

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    
    ## what does this do?
    authors = relationship('Author', backref='country')
      
    def __init__(self, name, capital=None):
      self.name = name
      self.capital = capital
    
    def __repr__(self):
      return "<Country('%s')>" % (self.name)

# First time create tables
Base.metadata.create_all(engine) 

# Check Country table
Country.__table__  

# Create instances of Book, Author, and Country
book1=Book('war and peace')
author1=Author('tolstoy')
country1=Country('russia')

print(book1)
print(author1)
print(country1)

# Add author to book
book1.author=author1
# Add country to author
author1.country=country1

print(book1)
print(author1)
print(author1.books)
print(country1.authors)


# Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Add data
session.add(book1)
session.add(author1)
session.add(country1)

# change db
session.commit()


# Get all authors
all_authors = session.query(Author).all()

# Print author's name and country 
for author in all_authors:
    print(author.name, author.country.name)

# Add two more books
book2=Book('anna karenina')
book2.author=author1
session.add(book2)
book3=Book('tale of two cities')
session.add(book3)
 
# Print Books
for b in session.query(Book):
    print(b)

# Print Authors
for a in session.query(Author):
    print(a)

# Print Book and Author
for row in session.query(Book, Author):
    print(row)
# Wait, Dickens wrote tale of two cities. 
# The information from Author is recycled 
  
# Using .join, we can print books with authors
for book in session.query(Book).join(Author):
    print(book.name, book.author.name)
# notice, no tale of two cities

session.commit()

author2 = Author('dickens')
book3.author = author2
for book in session.query(Book).join(Author):
    print(book.name, book.author.name)


# Copyright of the original version:

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.