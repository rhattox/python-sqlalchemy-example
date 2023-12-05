from models.User import User as User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# default
engine = create_engine("postgresql://postgres:postgres@db:5432/python_database", echo=True)

User.metadata.create_all(engine)



with Session(engine) as session:
    user1 = User(
        name="Bruno",
        email="bruno@com",
        password="123"
    )

    session.add_all([user1])
    session.commit()