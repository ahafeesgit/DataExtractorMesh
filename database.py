
import sqlite3

class Database:

   def getDatabaseConnection():
        database = sqlite3.connect('data/dataextractormesh.db')
        cursor = database.cursor()
        return database,cursor

