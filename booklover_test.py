import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # Add a book and test if it is in `book_list`.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        lover.add_book("The Great Gatsby", 5)
        self.assertTrue("The Great Gatsby" in lover.book_list['book_name'].values)

    def test_2_add_book(self):
        # Add the same book twice. Test if it's in `book_list` only once.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        lover.add_book("1984", 4)
        lover.add_book("1984", 4)
        occurrences = lover.book_list['book_name'].value_counts().get("1984", 0)
        self.assertEqual(occurrences, 1)

    def test_3_has_read(self):
        # Pass a book in the list and test if the answer is `True`.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        lover.add_book("To Kill a Mockingbird", 5)
        self.assertTrue(lover.has_read("To Kill a Mockingbird"))

    def test_4_has_read(self):
        # Pass a book NOT in the list and use `assertFalse` to test if the answer is `True`.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        self.assertFalse(lover.has_read("Moby Dick"))

    def test_5_num_books_read(self):
        # Add some books to the list, and test `num_books` matches expected.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        books = [("Book A", 3), ("Book B", 4), ("Book C", 5)]
        for book, rating in books:
            lover.add_book(book, rating)
        self.assertEqual(lover.num_books, len(books))

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some have rating > 3.
        # Test that the returned books have rating > 3.
        lover = BookLover("Test User", "testuser@example.com", "Fiction")
        books = [
            ("Book A", 2),
            ("Book B", 5),
            ("Book C", 4),
            ("Book D", 3),
            ("Book E", 5)
        ]
        for book, rating in books:
            lover.add_book(book, rating)
        fav_books = lover.fav_books()
        # Check that all ratings in fav_books are greater than 3.
        self.assertTrue(all(fav_books['book_rating'] > 3))
        # Check that fav_books contains the correct books.
        expected_fav_books = ["Book B", "Book C", "Book E"]
        self.assertEqual(set(fav_books['book_name']), set(expected_fav_books))

if __name__ == '__main__':
    unittest.main(verbosity=3)
