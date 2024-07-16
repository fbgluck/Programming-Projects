# This program will initialize the existing database by creating the required tables
# REF: https://www.sqlite.org/lang.html (SQL Lite Language)
# REF: https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/
# REF: https://www.tutorialspoint.com/execute_sql_online.php
import sqlite3
import os

dbDirName="projects\database_project\database" # folder name that will contain the database
dbFileName='studentLunch.db' # sets the name of the database

# change to project directory
os.chdir(dbDirName)

# connect to database
try:
    # create database connection using cannonical path
    obj_db_connection = sqlite3.connect(os.path.realpath(dbFileName))
    print (f"\n** Database studentLunch connected successfully")
except Exception as ex :
    print (f"ERROR: Unable to connect to database (Has it been created?)")
    print (f"Error raised was: {ex}")

# Drop Database tables
# obj_db_connection.execute('''DROP TABLE PARENTS;''')
# obj_db_connection.execute('''DROP TABLE RELATIONSHIP;''')

#Create Database tables    

# Create Student Table
try:
    obj_db_connection.execute(''' CREATE TABLE IF NOT EXISTS STUDENTS
                            (STUDENTID    INT PRIMARY KEY NOT NULL,
                            LASTNAME      TEXT            NOT NULL,
                            FIRSTNAME     TEXT            NOT NULL); ''')
except sqlite3.Error as error:
    print (f"\n** Failed to execute table create query: {error}")

# Create Parents Table
try:
    obj_db_connection.execute(''' CREATE TABLE IF NOT EXISTS PARENTS
                              (PARENTID     INT PRIMARY KEY NOT NULL,
                              STUDENTID     INT REFERENCES STUDENTS (STUDENTID),
                              RELATIONSHIPCODE INT REFERENCES RELATIONSHIP(RELATIONCODE),
                              PARENTLAST    TEXT            NOT NULL,
                              PARENTFIRST   TEXT            NOT NULL);''')
except sqlite3.Error as error:
    print (f"\n** Failed to execute table create query: {error}")

# Create Relationship Table
try:
    obj_db_connection.execute(''' CREATE TABLE IF NOT EXISTS RELATIONSHIP
                              (RELATIONCODE INT PRIMARY KEY NOT NULL,
                              RELATIONDESC  TEXT            NOT NULL);''')
except sqlite3.Error as error:
    print (f"\n** Failed to execute table create query: {error}")

# Create TransactionType Table
try:
    obj_db_connection.execute(''' CREATE TABLE IF NOT EXISTS TRANSACTIONTYPE
                              (TRANSTYPE INT PRIMARY KEY NOT NULL,
                              TRANSDESC  TEXT            NOT NULL);''')
except sqlite3.Error as error:
    print (f"\n** Failed to execute table create query: {error}")

# Create Transaction Table
try:
    obj_db_connection.execute(''' CREATE TABLE IF NOT EXISTS TRANS
                              (TRANSID   INT PRIMARY KEY NOT NULL,
                              STUDENTID  INT REFERENCES STUDENTS(STUDENTID),
                              TRANSTYPE  INT REFERENCES TRANSACTIONTYPE(TRANSTYPE),
                              TRANSDATE  TEXT   NOT NULL,
                              TRANSAMOUNT REAL NOT NULL);''')
except sqlite3.Error as error:
    print (f"\n** Failed to execute table create query: {error}")    
# ===============================================

#  Queries to be executed
#  Show All Tables in the Database
qryShowTables = ''' SELECT name FROM sqlite_master 
    where type = "table";'''
# Show structure of table RELATIONSHIP
qryShowStructure = '''SELECT SQL from sqlite_schema where name = "RELATIONSHIP";'''

# Execute queries to get information about the database
obj_db_cursor = obj_db_connection.cursor()
obj_db_cursor.execute(qryShowTables)
print(30*'=')
print ("Existing Database Tables:")
print(obj_db_cursor.fetchall())

obj_db_cursor.execute(qryShowStructure)
print(30*'=')
print ("PARENTS TABLE INFO:")
print(obj_db_cursor.fetchall())


# Close database
obj_db_connection.close()
print(f"\nDatabase {dbFileName} closed....")