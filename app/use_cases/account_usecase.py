from typing import List, Optional
from uuid import UUID
from app.domain.account import Account


class AccountUseCase:
    def __init__(self, account_repo):
        self.account_repo = account_repo

    def get_accounts(self) -> List[Account]:
        return self.account_repo.get_all_accounts()

    def create_account(self, account: Account) -> Account:
        return self.account_repo.add_account(account)

    def update_account(self, account_id: UUID, account: Account) -> Optional[Account]:
        return self.account_repo.update_account(account_id, account)

    def delete_account(self, account_id: UUID) -> bool:
        return self.account_repo.delete_account(account_id)
