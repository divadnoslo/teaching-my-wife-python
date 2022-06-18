# Practice Assignment 2 - Problem 2 Solution
print("\n\t\tPractice Assignment 2: Problem 2 Solution\n")

# Provide Weight Data
weightData = [230.0, 232.5, 228.7, 229.5, 231.7, 230.4, 234.1]

# Find the Average
numSamples = len(weightData)
sumWeightData = sum(weightData)
averageWeight = sumWeightData / numSamples

# Print Results
print(f"Weight Data Average: {averageWeight:.2f}\n")