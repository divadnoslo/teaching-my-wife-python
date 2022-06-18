# Practice Assignment 2 - Problem 3 Solution
print("\n\t\tPractice Assignment 2: Problem 3 Solution\n")

# Make the list
scram = 'biyoveualybo'
print(f"Scrambled Message: {scram}")

# Unscramble the List
newList = list("")

newList.append(scram[1])
newList.append(" ")

newList.append(scram[-4])
newList.append(scram[-1])
newList.append(scram[4])
newList.append(scram[5])
newList.append(" ")

newList.append(scram[2])
newList.append(scram[3])
newList.append(scram[6])
newList.append(" ")

newList.append(scram[-2])
newList.append(scram[-5])
newList.append(scram[0])
newList.append(scram[-3])
newList.append("!")

# Print Results
print(f"Unscrambled Message: {newList}\n")


