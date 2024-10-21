from typing import List, Optional
from app.domain.account import Account
from uuid import UUID, uuid4
from app.exceptions.account_exceptions import (
    AccountNotFoundException,
    AccountAlreadyExistsException,
)


class AccountRepository:
    def __init__(self):
        self.accounts_db = [
            Account(
                id=uuid4(),
                name="Cuenta de Nicole",
                account_type="Ahorro",
                balance=1000.0,
            ),
            Account(
                id=uuid4(),
                name="Cuenta de Jeymy",
                account_type="Corriente",
                balance=500.0,
            ),
        ]

    def get_all_accounts(self) -> List[Account]:
        return self.accounts_db

    def add_account(self, account: Account) -> Account:
        if any(acc.name == account.name for acc in self.accounts_db):
            raise AccountAlreadyExistsException(account.name)

        account.id = uuid4()
        self.accounts_db.append(account)
        return account

    def update_account(self, account_id: UUID, account: Account) -> Optional[Account]:
        for acc in self.accounts_db:
            if acc.id == account_id:
                acc.name = account.name
                acc.account_type = account.account_type
                acc.balance = account.balance
                return acc
        raise AccountNotFoundException(account_id)

    def delete_account(self, account_id: UUID) -> bool:
        account_to_delete = next(
            (acc for acc in self.accounts_db if acc.id == account_id), None
        )
        if account_to_delete:
            self.accounts_db.remove(account_to_delete)
            return True
        raise AccountNotFoundException(account_id)
