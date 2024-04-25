import book


class BookNotFoundError(Exception):
    pass


class MemberNotFoundError(Exception):
    pass


class BookAlreadyBorrowedError(Exception):
    pass


class BookNotInLibraryError(Exception):
    pass


class Library:
    """
        Represents a library.

        Attributes:
            books (dict): A dict of books in the library and the number of books there are. Book: number of books
            members (list): A list of members of the library.

    """

    def __init__(self, name):
        """
        Initializes a new Library instance.
        """
        self.name = name
        self.catalog = {}
        self.members = []

    def __iter__(self):
        """
        Generator to iterate over all books in the library.
        """
        for book_title, quantity in self.catalog.items():
            for _ in range(quantity):
                yield book_title

    def add_book(self, book):
        """
        Adds book title as key to catalog dictionary

        Args:
            book (Book): The book added to library
        """
        if book.title in self.catalog.keys():
            self.catalog[book.title] += 1
        else:
            self.catalog[book.title] = 1

    def remove_book(self, book):
        """
        Allows a member to borrow a book from the library.

        Args:
            book (Book): The book to be removed from library.

        Raises:
            BookNotFoundError: If the specified book is not found in the library.
            BookAlreadyBorrowedError: If the specified book is already borrowed by another member.
        """
        if book.title in self.catalog.keys():
            if self.catalog[book.title] > 1:
                self.catalog[book.title] -= 1
            elif self.catalog[book.title] == 0:
                del self.catalog[book.title]
        else:
            raise BookNotFoundError("Book has not been found in this library")

    def borrow_book(self, book, member):
        """
        Checks for book availability in catalog dict and if member exists

        Args:
            book (Book): Book that is getting borrowed from library
            member (Member): Member who is borrowing book from library
        """
        if book.title in self.catalog.keys() and member in self.members:
            if self.catalog[book.title] > 0:
                self.catalog[book.title] -= 1
                book.checkout(member)
                member.check_out.append(book.title)
            else:
                raise BookAlreadyBorrowedError("This book has been checked out. Please wait until it is returned")
        else:
            raise BookNotFoundError("Book has not been found in this library")

    def return_book(self, book, member):
        """
        Checks if book is already in catalog, increases value of book title, and reset borrowed_by, checkout_date, and due_date
        Args:
            book (Book): What book is returned
            member (Member): Member who returned book
        """
        if book.title in self.catalog.keys() and member in self.members:
            book.borrowed_by = None
            book.checkout_date = None
            book.due_date = None
            self.catalog[book.title] += 1
            member.checked_out.remove(book.title)
            print(f"Thank you for returning {book.title}")
        else:
            raise BookNotInLibraryError("This book does not belong to this library")

    def add_member(self, member):
        """
        Adds members to members list
        Args:
            member (Member): Member to be added to members list
        """
        self.members.append(member)

    def remove_member(self, member):
        """
        Removes members to members list
        Args:
            member (Member): Member to be removed from members list
        """
        self.members.remove(member)

    def calculate_late_fee(self, book, return_date=datetime.now().date()):
        """
        Calculates late fee for turning in book late at 10 cents per late day

        Args:
            book (Book): gets due date from returned book
            return_date (Datetime): what date the book was actually returned
        """
        late_rate = 0.1
        days_late = (book.due_date - return_date).days
        fee = days_late * late_rate
        if fee > 0:
            member.balance += fee

    @classmethod
    def total_books(cls):
        """
        Returns total number of books in the library
        """
        total = sum(self.values())
        return total

