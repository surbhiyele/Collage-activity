
import numpy as np
# Program 1: Array Indexing
arr = np.array([10, 20, 30, 40])

print("First element:", arr[0])
print("Last element:", arr[-1])

arr2 = np.array([[1, 2], [3, 4]])
print("Element:", arr2[0, 1])


# Program 2: Array Slicing
arr = np.array([10, 20, 30, 40, 50])
print("Sliced array:", arr[1:4])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Second column:", arr2[:, 1])


# Program 3: Reshaping
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print("Original array:", arr)
print("Reshaped array:\n", reshaped)


# Program 4: Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Program 5: Mathematical Operations
arr = np.array([1, 4, 9, 16])

print("Square root:", np.sqrt(arr))
print("Sum:", np.sum(arr))


# Program 6: Creating an Array
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)


# Program 7: Special Arrays
print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((3, 3)))
print("Full:\n", np.full((2, 2), 7))
print("Random:\n", np.random.rand(2, 2))


# Program 8: 2D Array Indexing and Slicing
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Indexing
print("Element:", arr[1][2])

# Slicing
print("Slice:\n", arr[0:2, 1:3])


# Program 9: Reshaping 2D Array
new_arr = arr.reshape(1, 9)
print("Reshaped:", new_arr)


# Program 10: Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean:", np.mean(a))
print("Sum:", np.sum(b))