# CS-162 Manipulating Arrays Python Assignment, Brent Grossman

import numpy as np

# Using NumPy to generate a random 2-dimensional, 5 by 5 array, using integers from 0 to 99
array = np.random.randint(0, 100, size=(5, 5), dtype=int)

# This prints the randomly generated array
print("Full Array:")
print(array, "\n")

# This prints the 2nd row and 3rd column number
print("The number from Row 2, Column 3 in the Array:")
# The array index parameters are 1, 2 because it starts at 0
print(array[1, 2], "\n")

# This adds up every numer within the array
array_sum = np.sum(array)

# This prints the sum of the array
print("The sum of all of the elements of the array:")
print(array_sum, "\n")

# This creates an array of the mean values for all the integers in each row
array_mean = np.mean(array, axis=1)

# This prints the mean values for each row in the array
print("The mean value of each row in the array:")
print(array_mean, "\n")

# This creates an array of the maximum values of each column in the array
array_column_max = np.max(array, axis=0)

# This prints the maximum value in each column of the array
print("The max value in each column:")
print(array_column_max, "\n")