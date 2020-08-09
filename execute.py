from Library_2 import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

library = Library()

while True:
    choice = input("Your choice :")
    if (choice == 'q'):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (choice == "1"):
        library.viewBooks()
    elif (choice == "2"):
        book_name = input("Which book do you want?")
        print("Book searching . . .")
        time.sleep(2)
        library.searchBooks(book_name)
    elif (choice == "3"):
        book_name = input("Book Name : ")
        author = input("Author : ")
        publisher = input("Publisher : ")
        genre = input("Genre : ")
        edition = input("Edition : ")
        new_book = Book(book_name, author, publisher, genre, edition)
        time.sleep(2)
        library.insertBook(new_book)
        print("Book inserted . . .")
    elif (choice == "4"):
        book_name = input("Which book do you want to delete?")
        answer = input("Are you sure about that ?(y/n) : ")
        if (answer == "y"):
            print("Book deleting...")
            time.sleep(2)
            library.deleteBook(book_name)
            print("Book deleted....")
    elif (choice == "5"):
        book_name = input("Which book do you want to increase edition ? :")
        print("Edition increasing . . .")
        time.sleep(2)
        library.increaseEdition(book_name)
        print("Edition increased . . .")
    else:
        print("Geçersiz İşlem...")
