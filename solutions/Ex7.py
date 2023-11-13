library_books = {
    'book1': {'title': 'Python Basics', 'author': 'John Smith', 'genre': 'Programming'},
    'book2': {'title': 'Data Science Essentials', 'author': 'Alice Johnson', 'genre': 'Data Science'},
    'book3': {'title': 'History of Science', 'author': 'Michael Turner', 'genre': 'History'},
    'book4': {'title': 'Cooking Mastery', 'author': 'Emily White', 'genre': 'Cooking'},
    'book5': {'title': 'Artificial Intelligence', 'author': 'David Lee', 'genre': 'Programming'},
}

# 1. Add a new book to the library
library_books['book6'] = {'title': 'Gardening for Beginners', 'author': 'Sarah Smith', 'genre': 'Gardening'}

# 2. Remove book3 from the library
del library_books['book3']

# 3. Change the genre of book4
library_books['book4']['genre'] = 'Cooking Basics'

# 4. Print the titles of all the books in the library
print("Titles of all books in the library:")
for book_id, book_info in library_books.items():
    print(book_info['title'])

# 5. Print the author of book1
print("Author of 'book1':", library_books['book1']['author'])

# 6. Return a book containing the title 'Data Science Essentials'
book_data_science = None
for book_info in library_books.values():
    if book_info['title'] == 'Data Science Essentials':
        book_data_science = book_info
        break
print("Book containing 'Data Science Essentials':", book_data_science)

# 7. Check if the library contains a book called 'Cryptography'
is_cryptography_present = any(book_info['title'] == 'Cryptography' for book_info in library_books.values())
print("Is 'Cryptography' present in the library?", is_cryptography_present)

# 8. Creating a new dictionary programming_books containing all books with the genre Programming
programming_books = {book_id: book_info for book_id, book_info in library_books.items() if book_info['genre'] == 'Programming'}
print("Programming Books:", programming_books)
