import base64
from repository.user_repository import UserRepository
from models import User
import logging

# setup Logging
logging.basicConfig(filename='web_app.log', encoding='utf-8', level=logging.DEBUG)


class UserServices:
    def __init__(self, email: str, password: str = None):
        self.email = email
        self.password = password

    def register_user(self) -> bool:
        """
        A function to add user details  to db
       
        Returns - 
        bool
        """

        # Check if User already exists 
        user = UserRepository().get_user(self.email)
        if user: 
            return False
        
        user = User(email = self.email, password = self.password)
        return UserRepository().add_user(user)
        
    
    def get_user_details(self) -> bool :
        """
        A function to fetch a user details from db

        Returns - 
        bool
        """
        user = UserRepository().get_user(self.email)

        if user and user.password == self.password:
                return True
        
        return False
        

