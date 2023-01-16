### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Dr. Seuss", "Stephen Colbert", "Patton Oswalt", "Stephen King", "Shel Silverstein", "Neil Gaiman", "IKEA"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append("Elmo")

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove("IKEA")
print(my_authors)
my_authors.pop()


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
print(my_authors[5])


# Now slice the list.

# Code here
# Example: my_authors[1:4]
print(my_authors[2:5])


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
my_authors_tuple = ("Dr. Seuss", "Stephen Colbert", "Patton Oswalt", "Stephen King", "Shel Silverstein", "Neil Gaiman", "IKEA")

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
my_authors_set = {"Dr. Seuss", "Stephen Colbert", "Patton Oswalt", "Stephen King", "Shel Silverstein", "Neil Gaiman", "IKEA"}
print(my_authors_set)

# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_authors_set.add("Puddles the Clown")
print(my_authors_set)


# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_authors_set.add("Puddles the Clown")
print(my_authors_set)



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

for author in my_authors:
    print(author)

for author in my_authors_tuple:
    print(author)

for author in my_authors_set:
    print(author)

