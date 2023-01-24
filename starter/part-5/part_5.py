### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# def user_added_book():
#     title = input("What's the title of the book? - ")
#     author = input("Who wrote the book? - ")
#     try:
#         year = int(input("When was the book written? - "))
#     except:
#         year = int(input("Please type an integer for the year. - "))
#     try:
#         rating = float(input("What rating out of 5 would you give the book? - "))
#     except:
#         rating = float(input("Please type a number for the rating. - "))
#     try:
#         pages = int(input("How many pages is the book? - "))
#     except:
#         pages = int(input("Please type an integer for the pages. - "))

#     with open("library.txt", "a") as f:
#         f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

# def view_books():
#     with open("library.txt", "r") as f:
#         file = f.readlines()

#         for line in file:
#             title, author, year, rating, pages = line.split(", ")

#             book_dictionary = {
#                 "title": title,
#                 "author": author,
#                 "year": year,
#                 "rating": rating,
#                 "pages": pages
#             }

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script



# def main_menu(lst):
    
#     running = True

#     while running:
        
#         choice = input("Type 1 to add a book. Type 2 to view all of the books. Type 3 to exit.  - ")

#         if choice == "1":
#             favorite_books.append(user_added_book())
#         elif choice == "2":
#             print(favorite_books)
#         elif choice == "3":
#             print("\nGoodbye.\n")
#             running = False
#         else:
#             print("\nPlease type 1 or 2.\n")

# if __name__ == "__main__":
#     main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def user_added_book(book_source):
    title = input("What's the title of the book? - ")
    author = input("Who wrote the book? - ")
    try:
        year = int(input("When was the book written? - "))
    except:
        year = int(input("Please type an integer for the year. - "))
    try:
        rating = float(input("What rating out of 5 would you give the book? - "))
    except:
        rating = float(input("Please type a number for the rating. - "))
    try:
        pages = int(input("How many pages is the book? - "))
    except:
        pages = int(input("Please type an integer for the pages. - "))

    with open(book_source, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages} \n")

def get_books(book_source):
    book_list = []
    with open(book_source, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            book_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return book_list

def view_books(book_source):
    for book in get_books(book_source):
        print(book)


def length_finder(book_source):
    max_pages = int(input("What is the maximum pages you'd like to read? - "))
    lst = get_books(book_source)
    for dict in lst:
        if dict["pages"] > max_pages:
            pass
        else:
            print(f'{dict["title"]} meet(s) the requested length requirement.')

def sort_high_to_low(book_source):
    lst = get_books(book_source)
    lst = sorted(lst, key=lambda x: int(x["rating"]), reverse = True)
    for book in lst:
        print(book)

def sort_low_to_high(book_source):
    lst = get_books(book_source)
    lst = sorted(lst, key=lambda x: int(x["rating"]), reverse = False)
    for book in lst:
        print(book)

def main_menu(book_source):
    
    running = True

    while running:
        
        choice = input("Type 1 to add a book. Type 2 to view all of the books. Type 3 to select a maximum booklength. Type 4 to sort books by rating high to low. Type 5 to sort books by rating low to high. Type 6 to exit.  - ")

        if choice == "1":
            user_added_book(book_source)
        elif choice == "2":
            view_books(book_source)
        elif choice == "3":
            length_finder(book_source)
        elif choice == "4":
            sort_high_to_low(book_source)
        elif choice == "5":
            sort_low_to_high(book_source)
        elif choice == "6":
            print("\nGoodbye.\n")
            running = False
        else:
            print("\nPlease type a number.\n")

if __name__ == "__main__":
    main_menu("library.txt")