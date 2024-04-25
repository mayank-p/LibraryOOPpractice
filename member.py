class Member:
    """
        Represents a member of the library.

        Attributes:
            name (str): The name of the member.
            membership_id (str): The membership ID of the member.
            balance (float): Indicates how much money is owed to the library
            checked_out (list): Stores what books member has checked out
    """
    def __init__(self, name, membership_id):
        """
        Initializes a new Member instance.

        Args:
            name (str): The name of the member.
            membership_id (str): The membership ID of the member.
        """

        self.name = name
        self.membership_id = membership_id
        self.balance = 0
        self.checked_out = []

    def __iter__(self):
        """
        Generator to iterate over all books in the checked out by member.
        """
        for book in self.checked_out:
            yield book

    def get_balance(self):
        """
        Returns member's balance
        """
        return self.balance


    def pay_balance(self, amount):
        """
        Indicates how much money member pays back library for fees

        Args:
            amount (float): The amount of money the member pays library
        """

        self.balance -= amount

