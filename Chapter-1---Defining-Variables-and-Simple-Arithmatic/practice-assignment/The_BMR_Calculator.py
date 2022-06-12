#Problem 3

# Variables to calculate BMR

# Assume gender is female
# Gender accounts for variable s -kcal/day-
s = -161

# Ask for weight of the individual
# Standard unit is in Kg 
weight = input("What is your weight in kg?:")

#Convert data type
weight = float(weight)

# Solve for weight variable
weight = 10*weight

# Print weight variable
print(f"Weight Variable: (weight) = {weight}")

# Ask for height
# Standard unit is in cm
height = input("What is your height?:")

#Convert data type
height = float(height)

# Solve for weight variable
height = 6.25*height

# Print height variable
print(f"Height Variable: (height) = {height}")

# Ask for age
age = input("What is your age?:")

#Convert data type
age = float(age)

# Solve for age variable
age = 5*age

# Print age variable
print(f"Age Variable: (age) = {age}")

# Solve for BMR
BMR = weight + height+ age + s

# Print BMR
print(f"Total # Kcals allotted per day: (BMR) = {BMR}")

