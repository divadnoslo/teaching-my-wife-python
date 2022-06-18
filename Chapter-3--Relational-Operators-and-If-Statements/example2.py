"""
Logical Operations!

Simliar to Relational Operators, but not quite the same. 

With relational operators, you learned to ask one question. 
But now, what if you have multiple questions? 

Logical operators can only operate on Boolean datatypes 
 (a.k.a. True and False)

Typically, the outputs of relational operators will serve
 as the inputs to logical operators.

There are 4 logical operators, but we will cover 2:
 - the AND (and) operation
 - the OR (or) operation

The 'and' operator returns 'True' only is ALL of it's inputs are true. 
Otherwise, it will return 'False'. 

The 'or' operator returns 'True' if at least ONE of it's inputs are true. 
Otherise, it will return 'False' if all the inputs are false. 
 """

 #================================================================
 # AND logical operations

 # Example 1
 # Let's say I'm trying to answer the question
 # "Do I deserve a beer with dinner?"
 #
 # To answer that questions, I might ask myself:
 #  - Did I exercise today?
 #  - Did I eat healthy today?
 #
 # If both of these answers are true, then I do deserve a beer. 
 # If one of these didn't happen, then I don't deserve a beer. 

print("\n\n")

print("\t\tThe 'and' Logical Operator Examples\n")

# Answer Set One
didIexercise = True
didIeatHealthy = True

print("Do I deserve a beer today? Answer Set 1\n")
print(f"Did I Exercise Today? {didIexercise}")
print(f"Did I Eat Healthy Today? {didIeatHealthy}")

 # Use the 'and' logical operator
doIdeserseBeer = (didIexercise and didIeatHealthy)
print(f"Determination: Dod I deserve a beer? {doIdeserseBeer}")

# Answer Set Two
didIexercise = True
didIeatHealthy = False

print("Do I deserve a beer today? Answer Set 2\n")
print(f"Did I Exercise Today? {didIexercise}")
print(f"Did I Eat Healthy Today? {didIeatHealthy}")

 # Use the 'and' logical operator
doIdeserseBeer = (didIexercise and didIeatHealthy)
print(f"Determination: Dod I deserve a beer? {doIdeserseBeer}")

print("\n\n")


#================================================================
 # OR logical operations

 # Example 1
 # Let's say I'm trying to answer the question
 # "Do I deserve a beer with dinner?"
 #
 # To answer that questions, I might ask myself:
 #  - Did I exercise today?
 #  - Did I eat healthy today?
 #
 # But different from the last example, now I'm going easier on myself.
 # If one of these answers are true, then I do deserve a beer. 
 # If both of these didn't happen, then I don't deserve a beer. 

print("\t\tThe 'or' Logical Operator Examples\n")

# Answer Set One
didIexercise = False
didIeatHealthy = True

print("Do I deserve a beer today? Answer Set 1\n")
print(f"Did I Exercise Today? {didIexercise}")
print(f"Did I Eat Healthy Today? {didIeatHealthy}")

 # Use the 'and' logical operator
doIdeserseBeer = (didIexercise or didIeatHealthy)
print(f"Determination: Dod I deserve a beer? {doIdeserseBeer}")

# Answer Set Two
didIexercise = False
didIeatHealthy = False

print("Do I deserve a beer today? Answer Set 2\n")
print(f"Did I Exercise Today? {didIexercise}")
print(f"Did I Eat Healthy Today? {didIeatHealthy}")

 # Use the 'and' logical operator
doIdeserseBeer = (didIexercise or didIeatHealthy)
print(f"Determination: Dod I deserve a beer? {doIdeserseBeer}")

print("\n\n")

#=================================================================
#
# Ok, this is great, but why is this different than relational operators?
# 
# Given the examples above, you probably could have achieved that same results. 
#
# But, here is where where logical operators are helpful. 
# 
# Relational operators can work on all datatypes, but logical operators
# only function on Boolean datatypes. Here is how both are typically applied. 
#
#==================================================================

# Relational & Logical Operators Together

# Again, I am trying to answer the question, do I deserve a beer?

# But now the criteria is different:
#   a.) Did I eat too many calories? (Let's say BMR is 2500)
#   b.) Did I exercise for long enough? (At least 60 minutes)
#   c.) Is it the weekend? (Let's say I'm only allowed to drink on the weekend)

# Let's say that condition A or B must be met, and C must always be met. 

print("\t\tRelational and Logical Operators Combined\n")

# Let's Set the Limits
BMR = 2500  # calories in a day
exerciseTime = 60 # minimum amount of workout time
print(f"My BMR is currently {BMR}")
print(f"I need to exercise for at least {exerciseTime} minutes a day\n")

# Answer Set One
calories = 2400
exercise = 30
isWeekend = True

# Print Answer Set
print("Answer Set #1")
print(f"How many calories did I consume today? {calories}")
print(f"How many minutes did I spend exercising? {exercise}")
print(f"Is it the weekend? {isWeekend}")

# Compute the answer in one line
answer = isWeekend and ((calories <= BMR) or (exercise >= exerciseTime))

# Print Results
print(f"Determination: Do I deserve a beer? {answer}\n\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Answer Set Two
calories = 2800
exercise = 75
isWeekend = True

# Print Answer Set
print("Answer Set #2")
print(f"How many calories did I consume today? {calories}")
print(f"How many minutes did I spend exercising? {exercise}")
print(f"Is it the weekend? {isWeekend}")

# Compute the answer in one line
answer = isWeekend and ((calories <= BMR) or (exercise >= exerciseTime))

# Print Results
print(f"Determination: Do I deserve a beer? {answer}\n\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Answer Set Three
calories = 2300
exercise = 75
isWeekend = False

# Print Answer Set
print("Answer Set #3")
print(f"How many calories did I consume today? {calories}")
print(f"How many minutes did I spend exercising? {exercise}")
print(f"Is it the weekend? {isWeekend}")

# Compute the answer in one line
answer = isWeekend and ((calories <= BMR) or (exercise >= exerciseTime))

# Print Results
print(f"Determination: Do I deserve a beer? {answer}\n\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Answer Set Four
calories = 2800
exercise = 30
isWeekend = True

# Print Answer Set
print("Answer Set #4")
print(f"How many calories did I consume today? {calories}")
print(f"How many minutes did I spend exercising? {exercise}")
print(f"Is it the weekend? {isWeekend}")

# Compute the answer in one line
answer = isWeekend and ((calories <= BMR) or (exercise >= exerciseTime))

# Print Results
print(f"Determination: Do I deserve a beer? {answer}\n\n")
