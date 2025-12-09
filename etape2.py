import numpy as np

tableau_1d = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau_1d)
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)
zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)
ones = np.ones((3, 2))
print("Ones :\n", ones)
progression = np.arange(0, 10, 2)  
print("np.arange :", progression)
linspace = np.linspace(0, 1, 5)  
print("np.linspace :", linspace)

print("tableau_1d + 5 :", tableau_1d + 5)
