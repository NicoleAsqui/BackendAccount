import pytest
from uuid import uuid4
from app.exceptions.account_exceptions import (
    AccountAlreadyExistsException,
    AccountNotFoundException,
)
from app.use_cases.account_usecase import AccountUseCase
from app.adapters.db.account_repository import AccountRepository
from app.domain.account import Account


@pytest.fixture
def account_repo():
    return AccountRepository()


@pytest.fixture
def account_usecase(account_repo):
    return AccountUseCase(account_repo)


def test_get_all_accounts(account_usecase):
    accounts = account_usecase.get_accounts()
    assert len(accounts) == 2


def test_create_account(account_usecase, account_repo):
    new_account = Account(
        id=uuid4(), name="Cuenta Prueba 001", account_type="Corriente", balance=500.0
    )
    created_account = account_usecase.create_account(new_account)

    assert created_account.name == "Cuenta Prueba 001"
    assert created_account.account_type == "Corriente"
    assert len(account_repo.accounts_db) == 3


def test_update_account(account_usecase, account_repo):
    account_id = account_repo.accounts_db[0].id
    updated_account = Account(
        id=account_id,
        name="Cuenta Actualizada",
        account_type="Corriente",
        balance=1200.0,
    )

    result = account_usecase.update_account(account_id, updated_account)

    assert result is not None
    assert result.name == "Cuenta Actualizada"
    assert result.account_type == "Corriente"
    assert result.balance == 1200.0


def test_delete_account(account_usecase, account_repo):
    account_id = account_repo.accounts_db[0].id
    result = account_usecase.delete_account(account_id)

    assert result is True
    assert len(account_repo.accounts_db) == 1


def test_add_existing_account(account_usecase):
    new_account = Account(
        id=uuid4(), name="Cuenta de Nicole", account_type="Corriente", balance=500.0
    )
    with pytest.raises(AccountAlreadyExistsException):
        account_usecase.create_account(new_account)


def test_update_nonexistent_account(account_usecase):
    non_existent_id = uuid4()
    updated_account = Account(
        id=non_existent_id,
        name="Cuenta Actualizada",
        account_type="Corriente",
        balance=1200.0,
    )

    with pytest.raises(AccountNotFoundException):
        account_usecase.update_account(non_existent_id, updated_account)


def test_delete_nonexistent_account(account_usecase):
    non_existent_id = uuid4()

    with pytest.raises(AccountNotFoundException):
        account_usecase.delete_account(non_existent_id)
