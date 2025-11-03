import os
from dotenv import load_dotenv

load_dotenv()  # load .env file

DB_HOST = os.getenv("DB_HOST", "localhost")  # Docker maps port to host port
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")