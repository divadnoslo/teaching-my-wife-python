"""
If-Statements!  Now the programming begins to get real.....

If-statements allow you to control what code is run under certian conditions
If-statements use the following syntax

if (this expression should eval to 'True'):
	<all code indented under this statement will be run>

Notice these things: 
 - the statement in '()' will evaluate to 'True' or 'False'
 - the ':' operator indicates that the applicable code will be indented
 - this is the first example of where "white space" matters in the python language

See why we had to talk about relational and logical operators first?

Let's look at the example below
"""
print("\n\n")
#-----------------------------------
# Example 1
print("\t\tExample 1\n")

# Set Numbers
a = 21
b = 42
print(f"a = {a}, b = {b}")

# Make If Statement - which one will be called?
if (a <= b):
	print("'a' is less than 'b'")

if (a > b):
	print("'a' is greater than 'b'")	

print("\n\n")

#-----------------------------------
"""
There is more to if-statements then just that though

There are also else-if and else follow-ons, which follow this structure

if (expression evaluates to True):
	<some code runs here>
	<as many lines as you'd like>
elif (expression evaluates to True):
	<different code can be run here>
	<again, as many lines as you'd like>
else:
	<this code acts as a 'catch all'>

All if-statements must start with 'if'
You can have as many 'elif' intermediate steps as you'd like
The 'else' is optional, but it must be the last one and can only be used once if so

Here are some more examples
"""

#-----------------------------------
# Example 2
print("\t\tExample 2\n")

# Set Numbers
a = 21
b = 42
print(f"a = {a}, b = {b}")

# Make If-Statement Block
if (a == b):
	print("'a' is equal to 'b'")
elif (a <= b):
	print("'a' is less than 'b'")
else:
	print("'a' is greater than 'b'")

print("\n\n")
#-----------------------------------
