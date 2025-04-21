import numpy as np
import matplotlib.pyplot as plt

'''
Les valeurs connues
=======================================
dynode1 = 100
dynode2 = 200
dynode3 = 300
dynode4 = 400
epsilon_o = 8.85 * 10^-12
=======================================
'''

"""
Calcul du potentiel
=======================================
Nous savons que pour une surface Q = A * densité
ou encore Q = sigma * da'

V(x, y) = (1/4*pi*epsilon_o)[intégrale](dx'*dy'/(x**2 + y**2)**0.5)
=======================================
"""

# =============================
# Paramètres géométriques du PM 
# =============================

N_dynodes = 6  # Nombre de Dynodes
a = 3.0        # Espace extérieur en x
b = 2.0        # Espace extérieur en y
c = 4.0        # Longueur des dynodes en x
d = 2.0        # Espace entre les dynodes
e = 0.2        # Largeur des dynodes en y
f = 6.0        # Hauteur du PM en y

# Les dynodes du haut doivent être centrées sur l’espacement entre les dynodes du bas
espace_centré = c/2 - d/2

# Décalage sur la 1ère dynode du haut pour quelle soit vis-à-vis l'espace
g = c - espace_centré

# Longueur totale du PM (en x)
longueur = 2*a + g + c*N_dynodes/2 + d*(N_dynodes/2 - 1)

# Hauteur totale du PM (en y)
hauteur = f


# ================================
# Points de discrétisation par mm
# ================================

n = 10  # Dimention en nombre de points pour la grille
n_x, n_y = int(longueur*n), int(hauteur*n)
print(f"En x: {n_x} points, En y: {n_y} points")


# ============================
# Initialisation de la grille
# ============================

V = np.zeros((n_x, n_y))
# Masque pour fixé le potentiel (True = fixé)
fixe = np.zeros_like(V, dtype=bool)

# Conditions frontières (contour à un potentiel de 0V)
V[0, :] = 0
V[-1, :] = 0
V[:, 0] = 0
V[:, -1] = 0
fixe[0, :] = True
fixe[-1, :] = True
fixe[:, 0] = True
fixe[:, -1] = True


# =====================================
# Emplacement des Dynodes sur la grille
# =====================================

# Dynodes par ligne
lignes = int(N_dynodes/2)

# Pour stocker les positions
dynode_bas = {}  
dynode_haut = {}
  
# Emplacement en x des dynodes du bas
for i in range(1, lignes + 1):
  début = int((a + c*(i-1) + d*(i-1)) * n)
  fin = int((a + c*(i) + d*(i-1)) * n)
  y = int(b)
  dynode_bas[i] = (début, fin, y)

# Emplacement en x des dynodes du bas
for i in range(1, lignes + 1):
  début = int((a + g + c*(i-1) + d*(i-1)) * n)
  fin = int((a + c*(i) + d*(i-1)) * n)
  y = int(f - b)
  dynode_haut[i] = (début, fin, y)


print(dynode_bas)
print(dynode_haut)