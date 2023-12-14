# NumPy Fundamentals for Data Science

import numpy as np

def create_numpy_array():
    # Creating a NumPy array from a Python list
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("NumPy Array:")
    print(a)
    print("Type:", type(a))
    print("Access Element at Index 1:", a[1])
    print("Slicing:", a[1:])
    print("Last Element:", a[-1])

def multi_dimensional_array():
    # Creating a multi-dimensional NumPy array
    a_mul = np.array([[[1, 2, 3, 1],
                      [4, 5, 6, 1],
                      [7, 8, 9, 1]],
                     [[1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1]]])
    print("Multi-dimensional Array:")
    print(a_mul)
    print("Shape:", a_mul.shape)
    print("Number of Dimensions:", a_mul.ndim)
    print("Size:", a_mul.size)
    print("Data Type:", a_mul.dtype)

def handle_different_data_types():
    # Handling different data types in a NumPy array
    # Case 1: String in the matrix
    a_str = np.array([[1, 2, 3],
                      [4, "hello", 6],
                      [7, 8, 9]])
    print("Data Type (String):", a_str.dtype)

    # Case 2: Dictionary in the matrix
    d = {'1': 'A'}
    a_obj = np.array([[1, 2, 3],
                      [4, d, 6],
                      [7, 8, "hello"]])
    print("Data Type (Object):", a_obj.dtype)

    # Case 3: Specifying data type explicitly
    a_explicit = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]], dtype="<U7")
    print("Data Type (Explicit):", a_explicit.dtype)

def array_creation_methods():
    # Different methods for creating arrays
    a_zeros = np.zeros((10, 5, 2))
    a_ones = np.ones((10, 5, 2))
    a_empty = np.empty((5, 5, 5))
    print("Zeros Array:")
    print(a_zeros)
    print("Ones Array:")
    print(a_ones)
    print("Empty Array:")
    print(a_empty)

def array_creation_and_operations():
    # Creating arrays and performing operations
    x_values_increment = np.arange(0, 100, 5)
    x_values_evenly = np.linspace(0, 100, 5)
    print("Incremental Values:")
    print(x_values_increment)
    print("Evenly Distributed Values:")
    print(x_values_evenly)

def handle_special_values():
    # Handling special values in NumPy
    print("NaN:", np.nan)
    print("Infinity:", np.inf)
    print("Is NaN (nan):", np.isnan(np.nan))
    print("Is Infinity (inf):", np.isinf(np.inf))
    print("Is NaN (sqrt(-1)):", np.isnan(np.sqrt(-1)))
    print("Is Infinity (array/0):", np.isinf(np.array([10]) / 0))

def array_operations():
    # Performing operations on NumPy arrays
    a1 = np.array([1, 2, 3])
    a2 = np.array([6, 7, 8])
    print("Multiplication by Scalar:")
    print(a1 * 5)
    print("Addition by Scalar:")
    print(a1 + 5)
    print("Element-wise Addition:")
    print(a1 + a2)
    print("Element-wise Division:")
    print(a1 / a2)

def broadcasting_example():
    # Broadcasting example
    a1 = np.array([1, 2, 3])
    a2 = np.array([[1], [2]])
    print("Broadcasting Example:")
    print(a1 + a2)

def elementwise_operations():
    # Element-wise operations on arrays
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("Element-wise Square Root:")
    print(np.sqrt(a))

def array_manipulation():
    # Array manipulation methods
    a = np.array([1, 2, 3])
    print("Appending Elements:")
    a = np.append(a, [7, 8, 9])
    print(a)
    print("Inserting Elements:")
    a = np.insert(a, 3, [4, 5, 6])
    print(a)

if __name__ == '__main__':
    # Choose the function to test
    array_manipulation()

