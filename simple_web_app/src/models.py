from ast import Expression
from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
import uuid

# Create SQLAlchemy Engine
sqlite_file_name = "user_details.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_file_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    # table columns
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4().int))
    email = Column(String, nullable = True)
    password = Column(String, nullable = False)

    def __repr__(self):
        return f"<UserDetails : {self.email}>"
    

# Create the tables
Base.metadata.create_all(engine)