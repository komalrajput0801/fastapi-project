from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# The string form of the URL is
#     ``dialect[+driver]://user:password@host/dbname[?key=value..]``, where
#     ``dialect`` is a database name such as ``mysql``, ``oracle``,
#     ``postgresql``, etc., and ``driver`` the name of a DBAPI, such as
#     ``psycopg2``, ``pyodbc``, ``cx_oracle`
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/user_posts"

# https://www.oreilly.com/library/view/essential-sqlalchemy-2nd/9781491916544/preface02.html
# To connect to a database, we need to create a SQLAlchemy engine. The SQLAlchemy engine creates
# a common interface to the database to execute SQL statements. It does this by wrapping a pool of
# database connections and a dialect in such a way that they can work together to provide uniform
# access to the backend database. This enables our Python code not to worry about the differences
# between databases or DBAPIs.

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# creates a database session i.e. ORM specific unlike the engine
# When working with the ORM, the session object is our main access point to the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this Base class will be used to create sqlalchemy models i.e. all
# sqlalchemy models will inherit this class
Base = declarative_base()
