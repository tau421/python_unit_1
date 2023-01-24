my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

book_list = [
    {
    "title": "book1",
    "rating": 4,
    "pages": 200
},
{
    "title": "book2",
    "rating": 2,
    "pages": 100
}
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_helper(dict):
    book_string = f'{dict["author"]} wrote {dict["title"]}; it was published in {dict["year"]}.  It is {dict["pages"]} pages long and has a user rating of {dict["rating"]}.'
    return book_string

book_helper(my_book)
print(book_helper(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title_helper(dict):
    title_string = f'The title of the book is {dict["title"]}.'
    return title_string

def book_author_helper(dict):
    author_string = f'The author of the book is {dict["author"]}.'
    return author_string

def book_year_helper(dict):
    year_string = f'The book was published in {dict["year"]}.'
    return year_string

def book_rating_helper(dict):
    rating_string = f'The book has a user rating of {dict["rating"]}.'
    return rating_string

def book_pages_helper(dict):
    pages_string = f'The book is {dict["pages"]} pages long.'
    return pages_string

print(book_title_helper(my_book))
print(book_author_helper(my_book))
print(book_year_helper(my_book))
print(book_rating_helper(my_book))
print(book_pages_helper(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def length_finder(lst, pages):
    for dict in lst:
        if dict["pages"] <= pages:
            return dict

def rating_filter(lst, rating):
    for dict in lst:
        if dict["rating"] >= rating:
            return dict

def random_book_suggestion(lst):
    import random
    suggestion = random.randint(0, (len(lst)-1))
    return (lst[suggestion]["title"])