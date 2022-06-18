"""
Relational Operators!

Relational operators return only one of two answers: true or false

Think of relational operators as analogous to asking a question, 
and the answer you got is either yes (true) or no (false)

These operators are important for if-statements and while/for loops!
"""

#===================================================================
# Relational Operator Demonstrations
#===================================================================
print("\n\n")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'equivalence' operator (==)
a = 7;
b = 7;
c = 3;

print("\t\tEquivalence Operator Examples\n")
print(f"a = {a}, b = {b}, c = {c}")

# Example 1
answer = (a == b);
print(f"Is 'a' equal (==) to 'b'? {answer}")

# Example 2
answer = (a == c);
print(f"Is 'a' equal (==) to 'c'? {answer}")

# Character Examples
charA = 'r'
charB = 'y'
charC = 'r'
print(f"\ncharA = '{charA}', charB = '{charB}', charC = '{charC}'")

# Example 1c
answer = (charA == charC);
print(f"Is charA equal (==) to charC? {answer}")

# Example 2c
answer = (charA == charB);
print(f"Is charA equal (==) to charB? {answer}")

print("\n\n")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'non-equivalence' operator (!=)
x = 3
y = 4
z = 3

print("\t\tNon-Equivalence Operator Examples\n")
print(f"x = {x}, y = {y}, z = {z}")

# Example 3
answer = (x != y);
print(f"Is 'x' NOT equal (!=) to 'y'? {answer}")

# Example 4
answer = (x != z);
print(f"Is 'x' NOT equal (!=) to 'z'? {answer}")

# Character Examples
charA = 'r'
charB = 'y'
charC = 'r'
print(f"\ncharA = '{charA}', charB = '{charB}', charC = '{charC}'")

# Example 1c
answer = (charA != charC);
print(f"Is charA NOT equal (!=) to charC? {answer}")

# Example 2c
answer = (charA != charB);
print(f"Is charA NOT equal (!=) to charB? {answer}")

print("\n\n")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'greater-than' operator (>)
a = 4;
b = 3;
c = 4;

print("\t\tGreater Than Operator Examples\n")
print(f"a = {a}, b = {b}, c = {c}")

# Example 5
answer = (a > b);
print(f"Is 'a' greater than (>) to 'b'? {answer}")

# Example 6
answer = (b > c);
print(f"Is 'b' greater than (>) to 'c'? {answer}")

# Example 7
answer = (a > c);
print(f"Is 'a' greater than (>) to 'c'? {answer}")

print("\n\n")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'less-than' operator (<)
a = 4;
b = 3;
c = 4;

print("\t\tLess Than Operator Examples\n")
print(f"a = {a}, b = {b}, c = {c}")

# Example 5
answer = (a < b);
print(f"Is 'a' less than (<) to 'b'? {answer}")

# Example 6
answer = (b < c);
print(f"Is 'b' less than (<) to 'c'? {answer}")

# Example 7
answer = (a < c);
print(f"Is 'a' less than (<) to 'c'? {answer}")

print("\n\n")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'greater-than-or-equal-to' operator (>=)
a = 4;
b = 3;
c = 4;

print("\t\tGreater Than Or Equal To Operator Examples\n")
print(f"a = {a}, b = {b}, c = {c}")

# Example 5
answer = (a >= b);
print(f"Is 'a' greater than or equal to (>=) to 'b'? {answer}")

# Example 6
answer = (b >= c);
print(f"Is 'b' greater than or equal to (>=) to 'c'? {answer}")

# Example 7
answer = (a >= c);
print(f"Is 'a' greater than or equal to (>=) to 'c'? {answer}")

print("\n\n")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The 'less-than-or-equal-to' operator (<)
a = 4;
b = 3;
c = 4;

print("\t\tLess Than Or Equal To Operator Examples\n")
print(f"a = {a}, b = {b}, c = {c}")

# Example 5
answer = (a <= b);
print(f"Is 'a' less than (<=) to 'b'? {answer}")

# Example 6
answer = (b <= c);
print(f"Is 'b' less than (<=) to 'c'? {answer}")

# Example 7
answer = (a <= c);
print(f"Is 'a' less than (<=) to 'c'? {answer}")

print("\n\n")

#=================================================================