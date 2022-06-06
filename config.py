import os
from dotenv import load_dotenv

load_dotenv()

DB_DIALECT = os.getenv('DB_DIALECT')
DB_DRIVER = os.getenv('DB_DRIVER')
DB_DRIVER = f'+{DB_DRIVER}' if DB_DRIVER else DB_DRIVER
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_PORT = f':{DB_PORT}' if DB_PORT else DB_PORT
DB_SCHEMA = os.getenv('DB_SCHEMA')

CONN_STR = f'{DB_DIALECT}{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}{DB_PORT}/{DB_SCHEMA}'
