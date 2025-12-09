alist = [0]*6  #crée une liste Python standard : [0, 0, 0, 0, 0, 0]. Les éléments sont des objets int Python.
print("liste :",alist)
import numpy as np 
tab_zeros=np.zeros(6)  #crée un tableau NumPy : [0., 0., 0., 0., 0., 0.]. Par défaut, les éléments sont des nombres à virgule flottante (float), ce qui les rend optimisés pour les calculs mathématiques.
print("tableau:",tab_zeros)

linspace = np.linspace(0, 1, 5)  
print("np.linspace :", linspace) # pour garantir la précision et la complétude de l'intervalle

tableau_9 = np.arange(9)
print("Taille du tableau :", tableau_9.size)
tableau_9=tableau_9.reshape((4, 3))
print("Tableau  :", tableau_9) # ValueError: cannot reshape array of size 9 into shape (4,3)


