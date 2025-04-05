# For the purpose of genrating the JWT token

from datetime import datetime, timedelta
import time
from typing import Dict, Optional
import jwt
import os
from dotenv import load_dotenv

# Loading the items from .env into the os environment
load_dotenv()

JWT_SECRET = os.environ["secret"]
JWT_ALGORITHM = os.environ["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def token_response(token: str):
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def sign_jwt(email: str) -> Dict[str, str]:
    '''
    Generating the token using the payload, secret & algorithem
    '''
    payload = {
        "email": email,
        "exp    ": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decode_jwt(token: str) -> dict:
    '''
    Decoding the jwt token
    '''
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    
    
