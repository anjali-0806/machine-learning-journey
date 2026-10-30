
# ==========================================
# MACHINE LEARNING JOURNEY
# Topic: Introduction to NumPy
# ==========================================

# Importing NumPy library
import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# Finding array dimensions
print("\nDimensions:")
print(arr.ndim)

# Finding array shape
print("\nShape:")
print(arr.shape)

# Finding number of elements
print("\nSize:")
print(arr.size)

# Mathematical operations
print("\nAddition:")
print(arr + 5)

print("\nMultiplication:")
print(arr * 2)

# Statistical operations
print("\nMean:")
print(np.mean(arr))

print("\nMaximum:")
print(np.max(arr))

print("\nMinimum:")
print(np.min(arr))

# Creating a 2D array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\n2D Array:")
print(matrix)

print("\nMatrix Shape:")
print(matrix.shape)
