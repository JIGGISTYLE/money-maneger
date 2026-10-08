from fastapi import FastAPI
from routes.transactions import transaction_router
from routes.auth import auth
from routes.gmail import gmail
from routes.accounts import accounts

app=FastAPI(title="Money Maneger endpoint",description="API endpoint for money maneger from my bank")

app.include_router(transaction_router)
app.include_router(auth)
app.include_router(gmail)
app.include_router(accounts)

@app.get("/")
def home():
    return {"message":"welcome to money maneger"}

