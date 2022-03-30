from sqlalchemy import create_engine
import pymysql
# import secrets

conn_str = "mysql+pymysql://root:lucas2201@localhost/DBCEUAZUL"

def conn():
    try:
        engine = create_engine(conn_str)
        print(" * Sucessfully connected to the database")
        return engine
    except:
        print(" * Cannot connect to database")

