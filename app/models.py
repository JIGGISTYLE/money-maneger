from os import name
from sqlmodel import SQLModel

class users(SQLModel,table=True):  # for login any one , number based or email based

    id
    phone_number # none or if number otp based
    google_email # none or if mail otp based
    password_hash

class users_settings(SQLModel,table=True):  # for login 

    user_id
    currency # list of string of diffent currency symbols
    date_format 
    .... # not thought yet

class transactions(SQLModel,table=True):
    kind # income/expense/transfer
    id 
    user_id # user id
    occured_at
    amount
    category : # choose any one, category.kind==income/category.kind==expense/null ( for transfer )
    account : accounts  # deafult(we spent from this type of account),for all income,expense,transfer
    to_account: accounts# only for transfer
    note : str
    source # manual entry or gmail or etc
    gmail_message_id # none or unique
    

class category(SQLModel,table=True): 

    user_id
    name #gamimg,health,petty cash ,etc
    kind # income/expense


class accounts(SQLModel,table=True):

    user_id
    kind : # cash,UPI,gpay,bank_transfer