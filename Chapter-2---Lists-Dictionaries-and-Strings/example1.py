''' List Examples '''
print('\n\n Example 3 \n_____________________________________________________')

#------------------------------------------------------------------------------
# Create a List
print('Part 1 \n')

# Build a List of Integers
a = [1, 2, 3, 4, 5] # Note the Square Brackets
print(a)

# Extract First Element
element1 = a[0]
print(element1)

# Extract Second Element
element2 = a[1]
print(element2)

# Change the 4th Element
a[3] = 7
print(a)

# Extract Last Element
elementLast = a[-1]
print(elementLast)

# Extract 2nd to Last Element
element2ndLast = a[-2]
print(element2ndLast)

# -----------------------------------------------------------------------------
# Tuple Example
print('\nPart 2 \n')

# Build a Tuple of Integers
a = (1, 2, 3, 4, 5) # Note the Paranthensis

# Extract First Element
element1 = a[0]
print(element1)

# Extract Second Element
element2 = a[1]
print(element2)

# Change the 4th Element
# a[3] = 7, tuples are immutable, meaning elements can not be changed once declared!

#------------------------------------------------------------------------------
# Build a Set
print('\nPart 3 \n')

message = "hello world"

# Make a List
l = list(message)
print(f"List: {l}")

# Make a Tuple
t = tuple(message)
print(f"Tuple: {t}")

# Make a Set
s = set(message) # Note squigaly brackets on output
print(f"Set: {s}") # Sets are non-ordered and mutable

#------------------------------------------------------------------------------
# Build a Dictionary
print('\nPart 4 \n')

# Make a Dict
position = {'x': 3, \
            'y': 4, \
            'z': -5}
print(position)

# Print the Y Position
print(position['y'])

# Change the Y Position
position['y'] = 7
print(position['y'])
