import numpy as np
import matplotlib.pyplot as plt
array1 = np.zeros(5)
array2 = np.array([1, 2, 3,np.nan, np.nan, 6])
print(array1)
print(np.isnan(array2))

new_array = np.nan_to_num(array1, nan = 10)
print(np.isnan(new_array))
print(new_array)

plt.plot(["x","y","z"], [10,20,30], marker = "o", color = "red", label = "plotting")
plt.legend()
plt.grid(True)
plt.show()