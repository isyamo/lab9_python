import numpy as np

tableau_float32 = np.array([1, 2, 3], dtype=np.float32)
print("Tableau tableau_float32 :", tableau_float32)
print("Type des éléments :", tableau_float32.dtype)

tableau_int32 = tableau_float32.astype(np.int32)
print("Tableau après astype(np.int32) :", tableau_int32)
print("Type des éléments après conversion :", tableau_int32.dtype)

print("Mémoire utilisée par tableau_float32 :", tableau_float32.nbytes, "bytes")
print("Mémoire utilisée par tableau_int32 :", tableau_int32.nbytes, "bytes")

tableau_eye = np.eye(4)
print("Eye :\n", tableau_eye)
tableau_full=np.full((2, 2), 7)
print("Full :\n", tableau_full)
tableau = np.arange(12).reshape((4, 3))
print("Tableau :\n", tableau)

tableau_multipliee = tableau * 10
print("Tableau après multiplication  :\n", tableau_multipliee)
print(np.sqrt(tableau_multipliee))

#L'intérêt de NumPy est d'offrir performance et simplicité de code pour les calculs numériques:
    #Vitesse : Opérations vectorisées (exécutées simultanément), beaucoup plus rapides.
    #Clarté : Permet des calculs complexes sur un tableau en une seule ligne, évitant les boucles for.