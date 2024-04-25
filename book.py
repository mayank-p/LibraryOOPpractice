from datetime import datetime, timedelta
class Book:
    """
        Represents a book in the library.

        Attributes:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            borrowed_by (Member or None): The member who has borrowed the book or None if not borrowed.
            checkout_date (Datetime or None): When the book was checked out
            due_date (Datetime or None): When the book is due
    """
    def __init__(self, title, author, genre):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed_by = None
        self.checkout_date = None
        self.due_date = None

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"Book: {self.title} by {self.author}, Genre: {self.genre}, Checked out: {self.checkout}"

    def checkout(self, member):
        """
        Sets when book is checked out and sets due date two weeks from checkout date
        Args:
            member (Member) = Member who chekced book out
        """
        self.checkout_date = datetime.now().date()
        self.due_date = self.checkout_date + timedelta(weeks=2)
        self.borrowed_by = (member.name, member.membership_id)

    def extend_due_date(self, book):
        """
        Extends due date by two weeks
        """
        if self.due_date:
            self.due_date = self.due_date + timedelta(weeks=2)