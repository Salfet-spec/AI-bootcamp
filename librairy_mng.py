library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author }

    library.append(book)
    print("Book added successfully!\n")




def remove_book():
    title = input("Enter the title of the book to remove: ")

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return

    print("Book not found!\n")




def search_book():
    keyword = input("Enter title or author to search: ")

    found = False

    for book in library:
        if (keyword.lower() in book["title"].lower() or
                keyword.lower() in book["author"].lower()):
            print(f"Title : {book['title']}")
            print(f"Author: {book['author']}")
            print()
            found = True

    if not found:
        print("No matching books found.\n")




def display_books():
    if len(library) == 0:
        print("Library is empty.\n")
        return

    print("\nAvailable Books:")
    

    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']}")

    print()




while True:
    print(" Library Management System ")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        display_books()

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.\n")