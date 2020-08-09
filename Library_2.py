import sqlite3
import time


class Book:
    def __init__(self, book_name, author, publisher, genre, edition):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return "Book Name: {}\n" \
               "Author : {}\n" \
               "Publlisher : {}\n" \
               "Genre : {}\n" \
               "Edition : {}\n".format(self.book_name, self.author, self.publisher, self.genre, self.edition)


class Library():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("Library.db")
        self.cursor = self.connection.cursor()
        query = "create table if not exists Books (Name TEXT, Author TEXT, Publisher TEXT, Genre TEXT, Edition INT)"
        self.cursor.execute(query)
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def viewBooks(self):
        query = "select * from Books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No book in the library")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def searchBooks(self, book_name):
        query = "select * from Books where book_name = ?"
        self.cursor.execute(query, (book_name,))
        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No book in the library")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def insertBook(self, book):
        query = "Insert into Books values(?,?,?,?,?)"
        self.cursor.execute(query, (book.book_name, book.author, book.publisher, book.genre, book.edition))
        self.connection.commit()

    def deleteBook(self, book_name):
        query = "delete from Books where name = ?"
        self.cursor.execute(query, (book_name,))
        self.connection.commit()

    def increaseEdition(self, book_name):
        query = "select * from Books where name = ?"
        self.cursor.execute(query, (book_name,))
        books = self.cursor.fetchall()
        if (len(books) == 0):
            print("No book in the library")
        else:
            edition = books[0][4]
            edition += 1
            query2 = "update Books set edition = ? where name = ?"
            self.cursor.execute(query2, (edition, book_name))
            self.connection.commit()
