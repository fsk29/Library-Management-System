class Library:
    def __init__(self, filename="books.txt"):
        self.filename=filename
        self.file = open(self.filename, "a+")
        self.file.seek(0)


    def __del__(self):
        if self.file:
            self.file.close()

    def ListBooks(self):
        lines = self.file.readlines()
        books_info = [line.strip() for line in lines]
        for book_info in books_info:
            book_name, author, release_year, numberofpages = book_info.split(",")
            print(f"Book: {book_name}, Author: {author}, Release Year: {release_year}, Pages: {numberofpages}")


    def AddBook(self):
        name = input("Write the book name:")
        if name.lower() == 'q':
            return
        author = input("Write author name:")
        release_year = input("Write the book's release year:")
        numberofpages = input("Write how many pages in the book:")

        book_info = f"{name},{author},{release_year},{numberofpages}\n"

        self.file.write(book_info)
        print("Book has been added succesfully.")

    def RemoveBook(self):
        name = input("Write the name of the book you want to delete")
        if name.lower() == 'q':
            return
        self.file.seek(0)
        lines = self.file.readlines()
        books_info = [line.strip() for line in lines]

        books_list = [book_info.split(",") for book_info in books_info]


        indexes_to_remove = []
        for index, book in enumerate(books_list):
            if book[0] == name:
                indexes_to_remove.append(index)

        for index in sorted(indexes_to_remove, reverse=True):
            del books_list[index]

        self.file.seek(0)
        self.file.truncate()

        for book in books_list:
            book_info = ",".join(book) + "\n"
            self.file.write(book_info)
        
        print(f"{len(indexes_to_remove)} book(s) removed successfully.")


    

lib = Library()
menu = """
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
4) Press "q" to quit
"""

while True:
    choice = input(menu + "Enter your choice: ")

    if choice == "1":
        lib.ListBooks()
    elif choice == "2":
        lib.AddBook()
    elif choice == "3":
        lib.RemoveBook()
    elif choice.lower() == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")