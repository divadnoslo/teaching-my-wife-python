# Practice Assignment 2 - Problem 4 Solution
print("\n\t\tPractice Assignment 2: Problem 4 Solution\n")

# Build the List Row-by-Row
chart = [["Mike", "Hawk", 200.57, 46, 2000], \
         ["Ineada", "Dickens", 120.35, 27, 1800], \
         ["Big", "Johnson", 350.14, 54, 2500]]

# Print the Chart
print(chart)

#-------------------------------------------------------

# Find the Average Weights of the Patients
weights = [chart[0][2], chart[1][2], chart[2][2]]
print("\nWeights of the Patients")
print(weights)

# Compute Average Weight
averageWeight = sum(weights) / len(weights)
print(f"Average Weight: {averageWeight:.2f}")

#-------------------------------------------------------

# Find the Average Ages of the Patients
ages = [chart[0][3], chart[1][3], chart[2][3]]
print("\nAges of the Patients")
print(ages)

# Compute Average Ages
averageAges = sum(ages) / len(ages)
print(f"Average Ages: {averageAges:.2f}")

#-------------------------------------------------------

# Find the Average BMRs of the Patients
BMRs = [chart[0][4], chart[1][4], chart[2][4]]
print("\nBMR's of the Patients")
print(BMRs)

# Compute Average BMRs
averageBMRs = sum(BMRs) / len(BMRs)
print(f"Average BMRs: {averageBMRs:.2f}\n")

#-------------------------------------------------------