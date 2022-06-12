# Problem #3 Solution

# Ask for Inputs
print("What's up girly girl...   wanna calculate your BMR?")
weight = float(input("Shh... wishper your weight in kilograms:  "))
height = float(input("And what's your height in centimeters:  "))
age = float(input("And you many years young?  "))

# Compute BMR
bmr = 655.0955 + (9.5634 * weight) + (1.8496 * height) + (4.6756 * age)

# Print Output
print("\n")
print("OMG GIRL!")
print(f"Your BMR is like totally {bmr}, you go glen-coco!")
