# all the manual transactions

from fastapi import APIRouter

#transaction handling
transactions=APIRouter(prefix="/transactions",tags=["transactions"])
