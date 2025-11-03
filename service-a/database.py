from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# This builds the connection string that SQLAlchemy uses to connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# Enables the connection through ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)