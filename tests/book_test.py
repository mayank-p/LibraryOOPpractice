import unittest



class TestMember(unittest.TestCase):
    def setUp(self):
        # Initialize a member instance for testing
        self.book = Book("Way of Kings", "Brandon Sanderson", "fantasy")

    def test_initialization(self):
        # Test if book is initialized correctly
        self.assertEqual(self.title, "Way of Kings")
        self.assertEqual(self.author, "Brandon Sanderson")
        self.assertEqual(self.genre, "Fantasy")
        self.assertIsNone(self.borrowed_by, None)
        self.assertIsNone(self.checkout_date, None)
        self.assertIsNone(self.due_date, None)

    def test_checkout(self):
        # Test if checkout sets checkout date, due date, and borrowed by correctly
        member = Member("Bob Smith", "1")
        self.book.checkout(member)
        self.assertEqual(book.borrowed_by, ("Bob Smith", "1"))
        self.assertIsNotNone(self.book.checkout_date)
        self.assertIsNotNone(self.book.due_date)

    def test_extend_due_date(self):
        # Test if extend_due_date extends due date correctly
        self.book.checkout_date = datetime.now().date() - timedelta(days=14)
        self.book.due_date = datetime.now().date()
        self.book.extend_due_date()
        self.assertEqual(self.book.due_date, datetime.now().date() + timedelta(days=14))

if __name__ == '__main__':
    unittest.main()