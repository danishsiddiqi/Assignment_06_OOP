class Book:
    total_books = 0

    @classmethod
    def increament_book_count(cls):
        cls.total_books += 1

Book.increament_book_count()
Book.increament_book_count()

print(Book.total_books)  # Output: 1
      