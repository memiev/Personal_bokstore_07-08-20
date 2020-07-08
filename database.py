import sqlite3


def create_book_table():
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books (NAME text primary key, AUTHOR text ,READ integer )")

    connect.commit()
    connect.close()


def insert_book(name, author):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ? ,0)', (name, author))  # SQL injection attack (if f" string)

    connect.commit()
    connect.close()


def get_all_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    # books = cursor.fetchall()  # fetch - донасям // [(name,author,read), (name, author, read)] return list of tuples
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # comprehension

    connection.close()
    return books


def mark_book_as_read(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET read=1 WHERE name = ? ", (name,))  # make sure that this is a tuple

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE name = ?", (name,))

    connection.commit()
    connection.close()


"""
Concerned with storing and retrieving books  form a CSV file
format of the CSV:

name,author,read\n
name,author,read\n
name,author,read\n
name,author,read\n
"""
# Целия код тук се нарича "interface" той крие цялата комплекстност и не пречи в main фаила.

# books_file = "books.txt"
#
#
# def add_book(name, author):
#     with open(books_file, mode="a") as file:  # "a" stands for append
#         file.write(f"{name},{author},{'0'}\n")
#
#
# def get_all_books():
#     with open(books_file, "r") as file:
#         lines = [line.strip().split(",") for line in file.readlines()]  # lists with sub lists
#         books = [
#             {"name": line[0], "author": line[1], "read": line[2]}
#             for line in lines
#         ]
#     return books
#
#
# def mark_book_as_read(book_name):
#     books = get_all_books()  #
#     for book in books:
#         if book["name"] == book_name:
#             book["read"] = "1"
#     _save_all_books(books)
#
#
# def _save_all_books(books):
#     with open(books_file, mode="w") as file:
#         for book in books:
#             file.write(f"{book['name']},{book['author']},{book['read']}\n")
#
#
# def delete_book(book_name):
#     books = get_all_books()
#     books = [book for book in books if book["name"] != book_name]
#     _save_all_books(books)


"""
Concerned with storing and retrieving books  form a list.
in-memory DATABASE not SQL
"""

# books = []
#
#
# def prompt_add_book(book_name, book_author):
#     books.append(
#         {
#             "name": book_name,
#             "author": book_author,
#             "read": False
#         }
#     )
#
#
# def list_books():
#     for book in books:
#         check = "read" if book["read"] else "unread"
#         print(f"'{book['name']}' by {book['author']}, status: {check} ")
#
#
# def prompt_read(book_name):
#     for book in books:
#         if book["name"] == book_name and book["read"] is False:
#             book["read"] = True
#
#
# def delete_book(book_name):
#     global books
#     books = [book for book in books if book["name"] != book_name]

##########################################################
