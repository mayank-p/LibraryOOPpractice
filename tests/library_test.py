import unittest
import library

class TestMember(unittest.TestCase):
    def setUp(self):
        # Initialize a member instance for testing
        self.library = Library("Library")

    def test_initialization(self):
        # Test if library is initialized correctly
        self.assertEqual(self.name, "Library")
        self.assertEqual(self.catalog, {})
        self.assertEqual(self.members, [])


    def test_add_book(self):
        book1 = Book("Way of Kings", "Brandon Sanderson", "Fantasy")
        book2 = Book("Python", "Bob Smith", "Textbook")
        book3 = Book("Way of Kings", "Brandon Sanderson", "Fantasy")
        self.library.add_book(book1)
        self.assertEqual(self.library.catalog, {"Way of Kings": 1})
        self.library.add_book(book2)
        self.assertEqual(self.library.catalog, {"Way of Kings": 1, "Python": 1})
        self.library.add_book(book2)
        self.assertEqual(self.library.catalog, {"Way of Kings": 2, "Python": 1})

    def test_remove_book(self):
        book1 = Book("Way of Kings", "Brandon Sanderson", "Fantasy")
        book2 = Book("Python", "Bob Smith", "Textbook")

        self.library.add_book(book1)

        self.library.remove_book("Way of Kings")
        self.assertEqual(self.library.catalog, {})

        self.library.add_book(book1)
        self.library.add_book(book1)
        self.assertEqual(self.library.catalog, {"Way of Kings": 1})

        # Test if removing a non-existent book raises BookNotFoundError
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book(Book("Non-existent Book", "Author", "Genre"))

    def test_borrow_book(self):
        # Test borrowing a book from the library
        self.library.borrow_book(self.book1, self.member)
        self.assertEqual(self.library.catalog["Python Cookbook"], 0)
        self.assertIn("Python Cookbook", self.member.checked_out)

        # Test borrowing a book that is already borrowed
        with self.assertRaises(BookAlreadyBorrowedError):
            self.library.borrow_book(self.book1, self.member)

        # Test borrowing a non-existent book
        with self.assertRaises(BookNotFoundError):
            self.library.borrow_book(Book("Non-existent Book", "Author", "Genre"), self.member)

    def test_add_member(self):
        # Test if adding a member updates the members list correctly
        member1 = Member("John Doe", "M123")
        member2 = Member("Jane Doe", "M124")

        self.library.add_member(member1)
        self.assertEqual(self.library.members, [member1])

        self.library.add_member(member2)
        self.assertEqual(self.library.members, [member1, member2])



