# This file will create the project database
import sqlite3 # imports SQL Lite database
import os

dbDirName="projects\database_project\database" # folder name that will contain the databaase
dbFileName='studentLunch.db' # sets the name of the database
print(f'\n** Current working directory is: {os.getcwd()}') # get current working directory

# Check if required file structure exists
if os.path.exists(dbDirName):
    print (f"OK... {dbDirName} exists")
else:  # structure for database does not exist so create it under current working directory
    print(f"** {dbDirName} does not exist... creating structure")
    os.makedirs('projects\database_project\database')

os.chdir('projects/database_project/database')
print(f'\n** Working directory changed to: {os.getcwd()}') # changes working directory

try:
    # create database using cannonical path
    obj_db_connection = sqlite3.connect(os.path.realpath(dbFileName))
    print (f"\n** Database studentLunch created / connected successfully")
except Exception as ex :
    print (f"ERROR: Database not created or unable to connect")
    print (f"Error raised was: {ex}")

# Close database
obj_db_connection.close()
print(f'\n** Database {dbFileName} closed...')