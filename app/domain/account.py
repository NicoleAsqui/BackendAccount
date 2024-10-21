from pydantic import BaseModel
from uuid import UUID, uuid4


class Account(BaseModel):
    id: UUID = uuid4()
    name: str
    account_type: str
    balance: float
