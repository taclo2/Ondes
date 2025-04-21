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

N_dynodes = 12  # Nombre de Dynodes
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

V = np.zeros((n_y, n_x))
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


# Pour fixé le potentiel V[début_i : fin_i, début_j, fin_j] où i-> y et j-> x
# Emplacement des dynodes du bas
for i in range(0, lignes):

  début_x = int((a + c*(i) + d*(i)) * n)
  fin_x = int((a + c*(i+1) + d*(i)) * n)

  début_y = int(b * n)
  fin_y = int((b + e) * n)
  
  dynode_bas[i+1] = [(début_x, fin_x), (début_y, fin_y)]

  #Fixé le Potentiel
  V[début_y : fin_y, début_x : fin_x] = 100 + (i)*200
  fixe[début_y : fin_y, début_x : fin_x] = True


# Emplacement des dynodes du haut
for i in range(0, lignes):

  début_x = int((a + g + c*(i) + d*(i)) * n)
  fin_x = int((a + g + c*(i+1) + d*(i)) * n)

  début_y = int((f - b - e) * n)
  fin_y = int((f - b) * n)

  dynode_haut[i+1] = [(début_x, fin_x), (début_y, fin_y)]
  
  #Fixé le Potentiel
  V[début_y : fin_y, début_x : fin_x] = 200 + (i)*200
  fixe[début_y : fin_y, début_x : fin_x] = True


"""
=========================
Test pour potentiel fixé
==========================

print(dynode_bas)
print(dynode_haut)

plt.imshow(fixe, cmap="gray", origin='lower')
plt.title("Zones de potentiel fixé")
plt.colorbar()
plt.show()
"""


# ====================================
# Méthode de relaxation par le Jacobi
# ====================================

# Fonction qui effectue une itération de la méthode de Jacobi
# Approxime la solution de l'équation (nabla^2*V = 0 et Conditions Dirichelts)

def jacobi(V, fixe):
    V_new = V.copy()
    V_new[1:-1, 1:-1] = 0.25 * (V[1:-1, 2:] + V[1:-1, :-2] + V[2:, 1:-1] + V[:-2, 1:-1])
    V_new[fixe] = V[fixe]
    return V_new

#Boucle d'itération jusqu'à la convergence
def iter_jacobi(V, fixe, max_iter=10000, tol=1e-4):

  for i in range(max_iter):
      V_new = jacobi(V, fixe)
    
      if np.max(np.abs(V_new - V)) < tol:
          print(f"{i} itérations")
          break
      V = V_new

  return V

# Prendre le résultat des itérations
V_final = iter_jacobi(V, fixe)


# =================================
# Affichage graphique du potentiel
# =================================
plt.imshow(V_final, origin='lower', cmap='Reds', extent=[0, longueur, 0, hauteur])
plt.colorbar(label='Potentiel (V)')
plt.title("Potentiel électrostatique dans le tube PM")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.show()