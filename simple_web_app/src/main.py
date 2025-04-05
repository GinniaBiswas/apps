import base64
from fastapi import FastAPI, HTTPException, Form, Request, status, Depends
import logging
from fastapi.templating import Jinja2Templates
from services.user_service import UserServices
from fastapi.responses import RedirectResponse
from services.auth.auth_service import sign_jwt
import uvicorn
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# Creating a Fastapi object
app = FastAPI()

# For encrypting the password using a hasing mechanism
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Setting up Logging
logging.basicConfig(filename='web_app.log', encoding='utf-8', level=logging.DEBUG)

# To Render all templates from the templates folder
templates = Jinja2Templates(directory="templates")


# Endpoint for login
@app.get("/")
@app.get("/login")
async def login(request:Request):
    return templates.TemplateResponse("login.html",context={"request":request})

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):   
    encoded_password = base64.b64encode(password.encode('utf-8'))
    user_exists = UserServices(email=email, password=encoded_password).get_user_details()
    if user_exists:
        return sign_jwt(email)
    
    raise HTTPException(status_code=401, detail=f"Invalid credentials. Please register", headers={"WWW-Authenticate": "Bearer"})

# Welcome page
@app.get("/welcome")
async def welcome(request:Request):
    return templates.TemplateResponse("home.html",context={"request":request})


# Endpoint for Registering
@app.get("/register")
async def register(request:Request):
    return templates.TemplateResponse("registration.html",context={"request":request})

@app.post("/register")
async def register(request: Request, email: str = Form(...), password: str = Form(...)):
    encoded_password = base64.b64encode(password.encode('utf-8'))
    user_created = UserServices(email=email, password=encoded_password).register_user()
    if not user_created:
        raise HTTPException(status_code=401, detail="Unable to create User. User already exists!!")
    
    return RedirectResponse(request.url_for("login"), status_code=status.HTTP_303_SEE_OTHER) 


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)