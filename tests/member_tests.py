import unittest

class TestMember(unittest.TestCase):
    def setUp(self):
        # Initialize a member instance for testing
        self.member = Member("John Doe", "M123")

    def test_initialization(self):
        # Test if member is initialized correctly
        self.assertEqual(self.member.name, "John Doe")
        self.assertEqual(self.member.membership_id, "M123")
        self.assertEqual(self.member.balance, 0)
        self.assertEqual(self.member.checked_out, [])

    def test_get_balance(self):
        # Test if get_balance returns the correct balance
        self.assertEqual(self.member.get_balance(), 0)

    def test_pay_balance(self):
        # Test if pay_balance deducts the correct amount from balance
        self.member.balance = 10
        self.member.pay_balance(5)
        self.assertEqual(self.member.balance, 5)

    def test_iterate_checked_out_books(self):
        # Test if the __iter__ method yields checked out books correctly
        book1 = "Book 1"
        book2 = "Book 2"
        self.member.checked_out = [book1, book2]

        books = [book for book in self.member]
        self.assertEqual(books, [book1, book2])

if __name__ == '__main__':
    unittest.main()
