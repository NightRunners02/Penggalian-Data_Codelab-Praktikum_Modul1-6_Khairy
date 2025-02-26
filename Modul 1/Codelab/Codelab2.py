import numpy as np

nim_digits = [3, 7, 0, 3, 1, 1, 4, 3, 9]
array_2d = np.array(nim_digits).reshape(3, 3)
print("Array 2D:")
print(array_2d)

addition = array_2d + 2
subtraction = array_2d - 2
multiplication = array_2d * 2

print("\nHasil Pertambahan:")
print(addition)
print("\nHasil Pengurangan:")
print(subtraction)
print("\nHasil Perkalian:")
print(multiplication)

array_1d = array_2d.flatten()
print("\nArray 1D:")
print(array_1d)

sliced_array = array_2d[:2, 1:] 
print("\nHasil Slicing:")
print(sliced_array)
