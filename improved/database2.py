from .database_connection import DataBaseConnection


def create_book_table():
    # connect = sqlite3.connect("data.db")
    # cursor = connect.cursor()
    #
    # cursor.execute("CREATE TABLE IF NOT EXISTS books (NAME text primary key, AUTHOR text ,READ integer )")
    #
    # connect.commit()
    # connect.close()
    with DataBaseConnection("data2.db") as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books (NAME text primary key, AUTHOR text ,READ integer )")


def insert_book(name, author):
    with DataBaseConnection("data2.db") as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ? ,0)', (name, author))  # SQL injection attack (if f" string)


def get_all_books():
    with DataBaseConnection("data2.db") as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        # books = cursor.fetchall()  # fetch - донасям // [(name,author,read), (name, author, ...] return list of tuples
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # comprehension

    return books


def mark_book_as_read(name):
    with DataBaseConnection("data2.db") as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name = ? ", (name,))  # make sure that this is a tuple


def delete_book(name):
    with DataBaseConnection("data2.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name = ?", (name,))
