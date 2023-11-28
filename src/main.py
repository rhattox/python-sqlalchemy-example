import sqlalchemy
# import psycopg2
# print(psycopg2.__version__)
# print(sqlalchemy.__version__  )

from sqlalchemy import create_engine

# default
engine = create_engine("postgresql://postgres:postgres@db:5432/python_database")
print(engine)
from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(text("select username from users"))
    for row in result:
        print("username:", row.username)