import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.User import User

class TestUserCreation(unittest.TestCase):
    def test_create_user(self):
        db_url = 'postgresql://postgres:postgres@db:5432/python_database'
        engine = create_engine(db_url, echo=True)

        # Create the tables
        User.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()
        # Create a new user instance
        new_user = User(name='John Doe', email='john.doe@example.com', password='securepassword')

        # Add the user to the session
        session.add(new_user)

        # Commit the session to persist the user in the database
        session.commit()

        # Query the database to verify that the user was created
        queried_user = session.query(User).filter_by(email='john.doe@example.com').first()

        # Assert that the queried user exists and has the correct attributes
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.name, 'John Doe')
        self.assertEqual(queried_user.password, 'securepassword')
        user_to_delete = session.query(User).filter_by(id=queried_user.id).first()
        session.delete(user_to_delete)
        session.commit()
        session.close()

if __name__ == '__main__':
    unittest.main()
