### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def user_added_book():
    title = input("What's the title of the book? - ")
    author = input("Who wrote the book? - ")
    year = input("When was the book written? - ")
    rating = input("What rating out of 5 would you give the book? - ")
    pages = input("How many pages is the book? - ")

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def user_added_book():
    title = input("What's the title of the book? - ")
    author = input("Who wrote the book? - ")
    year = int(input("When was the book written? - "))
    rating = float(input("What rating out of 5 would you give the book? - "))
    pages = int(input("How many pages is the book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def user_added_book():
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

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

favorite_books = [
    {
        "title": "Green Eggs and Ham",
        "author": "Dr. Seuss",
        "rating": 5
    },
    {
        "title": "Where the Sidewalk Ends",
        "author": "Shel Silverstein",
        "rating": 4.5
    },
    {
        "title": "I Am America (and So Can You)",
        "author": "Stephen Colbert",
        "rating": 4.25
    }
]

def main_menu(lst):
    
    choice = input("Type 1 to add a book. Type 2 to view all of the books. - ")

    if choice == "1":
        favorite_books.append(user_added_book())
    elif choice == "2":
        print(favorite_books)
    else:
        print("\nPlease type 1 or 2.\n")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu(lst):
    
    running = True

    while running:
        
        choice = input("Type 1 to add a book. Type 2 to view all of the books. Type 3 to exit.  - ")

        if choice == "1":
            favorite_books.append(user_added_book())
        elif choice == "2":
            print(favorite_books)
        elif choice == "3":
            print("\nGoodbye.\n")
            running = False
        else:
            print("\nPlease type 1 or 2.\n")

main_menu(favorite_books)