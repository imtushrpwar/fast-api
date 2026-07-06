import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

# Create a SQLAlchemy engine to connect to the MySQL database.
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# 2. Safely encode the password so the '@' symbol doesn't break the URL structure
safe_password = urllib.parse.quote_plus(MYSQL_PASSWORD)


DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{safe_password}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
# CONNECTION
engine = create_engine(DATABASE_URL, echo=True)

#Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    # Dependency to get a database session.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# base
Base = declarative_base()