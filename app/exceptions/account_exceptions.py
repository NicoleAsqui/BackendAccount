class AccountNotFoundException(Exception):
    def __init__(self, account_id):
        self.account_id = account_id
        self.message = f"Account with ID {account_id} not found."
        super().__init__(self.message)


class AccountAlreadyExistsException(Exception):
    def __init__(self, account_name):
        self.account_name = account_name
        self.message = f"Account with name '{account_name}' already exists."
        super().__init__(self.message)
