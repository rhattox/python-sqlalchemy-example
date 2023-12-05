import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
from src.models.User import User
from sqlalchemy.orm import Session

class TestUserDelete(unittest.TestCase):
    def test_delete_user(self):
        db_url = 'postgresql://postgres:postgres@db:5432/python_database'
        engine = create_engine(db_url, echo=True)

        # Create the tables
        User.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        # Create a new user instance
        new_user = User(name='John Doe', email='john.doe@example.com', password='securepassword')

        user_to_delete = session.query(User).filter_by(id=1).first()
        session.delete(user_to_delete)
        session.close()

if __name__ == '__main__':
    unittest.main()
