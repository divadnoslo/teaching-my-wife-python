''' List Operation Examples '''
print('\n\n Example 5 \n_____________________________________________________')

#------------------------------------------------------------------------------
# Make A List

myList = ['a', 'b', 'c', 'd', 'e']
print(f"Origional List: {myList}")
print("\n")

#------------------------------------------------------------------------------
# Append a Letter to the List

myList.append('f')
print(f"Appended List: {myList}")
print("\n")

#------------------------------------------------------------------------------
# Extend Multiple Letters to the List

myList.extend(['g', 'h', 'i'])
print(f"Extended List: {myList}")
print("\n")

#------------------------------------------------------------------------------
# Insert the letter 'x' into the list at positon 1

myList.insert(1, 'x')
print(f"x Inserted in List: {myList}")
print("\n")

#------------------------------------------------------------------------------
# Remove the letter 'x' from the list

myList.remove('x')
print(f"x Removed from List: {myList}")
print("\n")

#------------------------------------------------------------------------------
# Pop the Letter 'd' from the List

letter_pop = myList.pop(3)
print(f"d Popped from the List: {myList}")
print(f"The letter popped: {letter_pop}")
print("\n")

#------------------------------------------------------------------------------
# Add some x's then count them

myList.insert(3, 'x')
myList.insert(5, 'x')
myList.insert(7, 'x')
numX = myList.count('x')
print(f"x's added to the list': {myList}")
print(f"Number of x's: {numX}")
print("\n")

#------------------------------------------------------------------------------
# Where is the letter e?

ind = myList.index('e')
print(f"The List': {myList}")
print(f"The letter e is in the {ind} position.")
print("\n")

#------------------------------------------------------------------------------
# Sort the List

myList.sort()
print(f"Sorted List: {myList}")
print("\n")

