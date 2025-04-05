# Repository for all "users" DB table related activities

from models import User, engine
from sqlalchemy.orm import Session
import logging

# Setup Logging
logging.basicConfig(filename='web_app.log', encoding='utf-8', level=logging.DEBUG)

class UserRepository:
    @staticmethod
    def add_user(user : User) -> bool:
        '''
        Adds user to the database

        Parameters - 
        user : "class User" type parameter
        
        '''
        try : 
            with Session(engine) as session:
                session.add(user)
                session.commit()
                return True
        except Exception as ex:
            logging.error(f"Database Error : {ex}")
        
        return False

    @staticmethod
    def get_user(email: str) -> User | None:
        '''
        Adds user to the database

        Parameters - 
        user : "class User" type parameter
        
        '''
        try : 
            with Session(engine) as session:
                user = session.query(User).where(User.email == email).first()
            return user
        except Exception as ex:
            logging.error(f"Database Error : {ex}")
        
        return None

