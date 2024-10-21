from fastapi import APIRouter, HTTPException
from typing import List
from app.domain.account import Account
from app.use_cases.account_usecase import AccountUseCase
from app.adapters.db.account_repository import AccountRepository
from uuid import UUID

router = APIRouter()

account_repo = AccountRepository()
account_usecase = AccountUseCase(account_repo)


@router.get("/accounts", response_model=List[Account])
def get_accounts():
    return account_usecase.get_accounts()


@router.post("/accounts", response_model=Account)
def create_account(account: Account):
    return account_usecase.create_account(account)


@router.put("/accounts/{account_id}", response_model=Account)
def update_account(account_id: UUID, account: Account):
    updated_account = account_usecase.update_account(account_id, account)
    if not updated_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return updated_account


@router.delete("/accounts/{account_id}")
def delete_account(account_id: UUID):
    success = account_usecase.delete_account(account_id)
    if not success:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": f"Account {account_id} deleted successfully"}
