# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here

names = []
ind = ['1st','2nd','3rd']

for x in range(3):
    names.append( input(f'Enter {ind[x]} name: ') )

order_names = names[:]
order_names.sort()

print( f'Originally entered names: {names}' )
print( f'Sorted names: {order_names}' )

### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### Your code here

word = input('Enter a word : ')
rev_word = word[-1::-1]

if word.lower() == rev_word.lower() :
    print( f'The word {word} is a palindrome' )
else :
    print( f'The word {word} is not a palindrome' )


### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome