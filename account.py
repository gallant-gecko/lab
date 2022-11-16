class Account:
    def __init__(self, name: str) -> None:
        """
        Function to initialize an account
        :param name: name to be given to account
        """
        self.__account_name = name
        self.__account_balance = 0.

    def deposit(self, amount: float) -> bool:
        """
        Function to allow account deposits
        :param amount: amount to be added to account
        :return: bool
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to allow account withdrawals
        :param amount: amount to be taken from account
        :return: bool
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        """
        Function to return account balance
        :return: float
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return account name
        :return: bool
        """
        return self.__account_name