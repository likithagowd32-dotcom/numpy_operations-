import numpy as np
import time

print("===== NUMPY OPERATIONS PROJECT =====")

# 1. Create numpy arrays
print("\n1. Creating Arrays")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 2. Different dimensions
print("\n2. Array Dimensions")
print("arr1 dimension:", arr1.ndim)
print("arr2 dimension:", arr2.ndim)

# 3. Mathematical operations
print("\n3. Mathematical Operations")
print("Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)

# 4. Broadcasting
print("\n4. Broadcasting")
b = np.array([10, 20, 30])
print("Broadcast result:\n", arr2 + b)

# 5. Statistical functions
print("\n5. Statistical Functions")
print("Mean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Standard Deviation:", np.std(arr1))
print("Max:", np.max(arr1))

# 6. NumPy vs Python list comparison
print("\n6. Performance Comparison (List vs NumPy)")

size = 1000000

# Python list timing
start = time.time()
list_data = list(range(size))
list_result = [x * 2 for x in list_data]
end = time.time()
print("Python List Time:", end - start)

# NumPy timing
start = time.time()
numpy_data = np.arange(size)
numpy_result = numpy_data * 2
end = time.time()
print("NumPy Time:", end - start)

# 7. Random data generation
print("\n7. Random Data")
random_array = np.random.rand(3, 3)
print("Random 3x3 Array:\n", random_array)

# 8. Optimized calculations (Vectorization)
print("\n8. Optimized Calculation")
large_array = np.arange(1, 1000000)
optimized_result = np.sum(large_array)
print("Sum of large array:", optimized_result)

# 9. Visualize array structure
print("\n9. Array Structure")
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")
