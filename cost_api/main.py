from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, date
from pydantic import BaseModel
import asyncpg 
import uvicorn
from datetime import datetime, timedelta


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
SECRET_KEY = "123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30000
DATABASE_URL = "postgresql://postgres:123@localhost:5432/cost_control"
# Hashing password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#-----------------------Model-------------------#
class User(BaseModel):
    login: str
    password: str
    email: str
    phone: str

class User_Auth(BaseModel):
    login: str
    password: str

class Income(BaseModel):
    user_id:int
    money: float
    date: date
    type_id: int

class Get_Income(BaseModel):
    user_id:int

class Delete_Income_by_id(BaseModel):
    id:int

class Get_Expenses_Type(BaseModel):
    id:int
class change_login_data(BaseModel):
    login: str
    user_id: int
class change_email_data(BaseModel):
    email:str
    user_id: int
class change_password_data(BaseModel):
    user_id: int
    old_pass: str
    new_pass: str

class Token(BaseModel):
    token: str
#----------------------Function--------------------------#

#DB Connection
async def connect_to_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")

#Close DB
async def close_db_connection(conn):
    await conn.close()

#create hash
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plained_password,hashed_password):
    return pwd_context.verify(plained_password, hashed_password)


#create access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


#--------------------End Function-------------------------#


#--------------------route-----------------------------#

#register user
@app.post('/register')
async def register_user(user: User):  
    conn = await connect_to_db()
    try:
        exist_user = await conn.fetch("""SELECT * FROM users WHERE login = $1 OR email = $2""", user.login, user.email)
        if exist_user:
           return {"message": 'user already exist!'}
        else:
            hashed_password = hash_password(user.password)
            await conn.execute("""INSERT INTO users(login,password,email,phone) 
                         VALUES($1,$2,$3,$4)""",user.login, hashed_password, user.email, user.phone)
            return {"message": 'Register Complete!'}
    except HTTPException:
        raise HTTPException(status_code=500, detail='Wrong data')
    finally:
        await close_db_connection(conn)

#Auth user
@app.post('/auth')
async def authorize_user(user:User_Auth):
    conn = await connect_to_db()
    try:
        acc = await conn.fetchrow("""SELECT * FROM users WHERE login = $1""",user.login)
        if not acc:
            raise HTTPException(status_code=500, detail="Wrong login or password")
        if not verify_password(user.password,acc["password"]):
            raise HTTPException(status_code=500, detail="Wrong login or password")
        else:
            access_token = create_access_token(data={"id": acc[0],
                                                 "login": acc[1],
                                                 "email": acc[3],
                                                 "phone":acc[4]
                                                 
                                                 },expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        
            return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException:
        raise HTTPException(status_code=500, detail="Wrong data")
    finally:
        await close_db_connection(conn)

#add income
@app.post('/add_income')
async def add_income(income: Income):
    conn = await connect_to_db()
    try:
        await conn.execute("""INSERT INTO income(user_id,money,date,type_id)
                     VALUES($1,$2,$3,$4)""",income.user_id,income.money,income.date,income.type_id)
        return{'message':'Your Balance Update!'}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Failed data")
    finally:
        await close_db_connection(conn)

#delete income
@app.post('/delete_income')
async def delete_income(income: Delete_Income_by_id):
    conn = await connect_to_db()
    try:
        await conn.execute("""DELETE FROM income WHERE id = $1""",income.id)
        return {'message':'Your Balance Update!'}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Failed data")
    finally:
        await close_db_connection(conn)

#get income order
@app.post('/get_income_by_id')
async def get_income_by_id(income:Get_Income):
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT * FROM income WHERE user_id = $1""",income.user_id)
        return {'incomes': data }
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)

#get income sum
@app.post('/get_sum_income')
async def get_sum_income(income:Get_Income):
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT SUM(money) FROM income WHERE user_id = $1""",income.user_id)
        return {'sum': data }
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)

#get expenses type
@app.get('/get_expenses_type')
async def get_expenses_type():
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT * FROM type_expenses""")
        return {'expenses_type': data}
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)

#add expenses 
@app.post('/add_expenses')
async def add_expenses(income: Income):
    conn = await connect_to_db()
    try:
        await conn.execute("""INSERT INTO expenses(user_id,money,date,type_id)
                     VALUES($1,$2,$3,$4)""",income.user_id,income.money,income.date,income.type_id)
        return{'message':'Your Balance Update!'}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Failed data")
    finally:
        await close_db_connection(conn)

#get expenses order by id
@app.post('/get_expenses_by_id')
async def get_expenses_by_id(income:Get_Income):
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT * FROM expenses WHERE user_id = $1""",income.user_id)
        return {'expenses': data }
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)

#get expenses type name
@app.get('/get_expenses_type_name')
async def get_expenses_type_name():
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT * FROM type_expenses""")
        return {'expenses_type': data}
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)

#delete expenses
@app.post('/delete_expenses')
async def delete_expenses(income: Delete_Income_by_id):
    conn = await connect_to_db()
    try:
        await conn.execute("""DELETE FROM expenses WHERE id = $1""",income.id)
        return {'message':'Your Balance Update!'}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Failed data")
    finally:
        await close_db_connection(conn)

#get sum of expenses
@app.post('/get_sum_expenses')
async def get_sum_expenses(income:Get_Income):
    conn = await connect_to_db()
    try:
        data = await conn.fetch("""SELECT SUM(money) FROM expenses WHERE user_id = $1""",income.user_id)
        return {'sum': data }
    except HTTPException:
        raise HTTPException(status_code=404, detail='Fatal error! Try Again!')
    finally:
        await close_db_connection(conn)




#Change Login
@app.put("/put_login")
async def change_login(user:change_login_data):
    conn = await connect_to_db()
    try:
        data = await conn.fetchrow("""SELECT * FROM users WHERE id = $1""", user.user_id)
        if not data:
            raise HTTPException(status_code=500, detail="Empty user")
        else:
            login = await conn.fetchrow("""SELECT * FROM users WHERE login = $1""",user.login)
            if login:
                raise HTTPException(status_code=500, detail="LOgin is taken")
            await conn.execute("""UPDATE users SET login = $1 WHERE id = $2""",user.login, user.user_id)
            return{"message": "Login update!"}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Wrong data")
    finally:
        await close_db_connection(conn)

#Change Email
@app.put("/change_email")
async def change_email(user: change_email_data):
    conn = await connect_to_db()
    try:
        data = await conn.fetchrow("""SELECT * FROM users WHERE id = $1""",user.user_id)
        if not data:
            raise HTTPException(status_code=500, detail="Email not found")
        else:
            login = await conn.fetchrow("""SELECT * FROM users WHERE login = $1""",user.email)
            if login:
                raise HTTPException(status_code=500, detail="LOgin is taken")
            await conn.execute("""UPDATE users SET email = $1 WHERE id = $2 """,user.email, user.user_id)
            return{"message":"Email Update!"}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Wrong data")
    finally:
        await close_db_connection(conn)


#Change password
@app.put("/change_password")
async def change_password(user: change_password_data):
    conn = await connect_to_db()
    try:
        data = await conn.fetchrow("""SELECT * FROM users WHERE id = $1""", user.user_id)
        if not data:
            raise HTTPException(status_code=500, detail="No userdata with this id")
        elif not verify_password(user.old_pass,data["password"]):
            raise HTTPException(status_code=500, detail="Old Password Wrong")
        else:
            hashed_password = hash_password(user.new_pass)
            await conn.execute("""UPDATE users SET password = $1 WHERE id = $2""",hashed_password, user.user_id)
            return{"message":"Password Changed!"}
            
    except HTTPException:
        raise HTTPException(status_code=500, detail="Wrong data")
    finally:
        await close_db_connection(conn)

#refresh token
@app.post('/refresh_token')
async def refresh_token(token : Token):
    token_data = jwt.decode(token.token,SECRET_KEY, algorithms=[ALGORITHM])
    email = token_data.get("email")
    conn = await connect_to_db()
    #check email is realy
    if not email:
        raise HTTPException(status_code=500, detail="Token dont have email or incorrect")
    try:
        user = await conn.fetchrow("""SELECT * FROM users WHERE email = $1""", email)
        if not user:
            raise HTTPException(status_code=500, detail="User with this email not register")
        else:
            access_token = create_access_token(data={"id": user["id"],
                                                 "login": user["login"],
                                                 "email": user["email"],
                                                 "phone":user["phone"]
                                                 
                                                 },expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
            return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        raise HTTPException(status_code=500, detail="Wrong data of token or his incorrect")
    finally:
        await close_db_connection(conn)



#---------------start---------------------------#
if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)