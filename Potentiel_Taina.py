import numpy as np
import matplotlib.pyplot as plt

"""
===================
Les valeurs connues
===================
dynode1 = 100
dynode2 = 200
dynode3 = 300
dynode4 = 400
epsilon_o = 8.85 * 10^-12

===================
Calcul du potentiel
===================
Avec la méthode itérative pour V(x, y)
"""


# =============================
# Paramètres géométriques du PM 
# =============================

N_dynodes = 4  # Nombre de Dynodes
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


# ===============================
# Points de discrétisation par mm
# ===============================

# n représente la résolution, nombre de pixel par mm
n = 20
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
def iter_jacobi(V, fixe, max_iter=10000, tol=1e-2):

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
plt.imshow(V_final, origin='lower', cmap='viridis', extent=[0, longueur, 0, hauteur])
plt.colorbar(label='Potentiel (V)', location='bottom')
plt.title("Potentiel électrostatique dans le tube PM")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.show()


#=================================
# Grille pour le champs électrique
#=================================

"""
V.shape[1] est la dimention de l'axe horizontale
V.shape[0] est la dimention de l'axe verticale
Par exemple V = np.zeros((2, 4)) alors V.shape donne (2, 4)
np.linspace(start, stop, num)
"""

x = np.linspace(0, longueur, V.shape[1]) 
y = np.linspace(0, hauteur, V.shape[0]) 
X, Y = np.meshgrid(x, y)


#==================
# Champs électrique
#==================

# np.gradiant renvoie [x, y]
# Metre 1/n pour avoir la valeur à la bonne échelle
Ey, Ex = np.gradient(-V_final, 1/n, 1/n)


#====================
# Affichage graphique
#====================

# Pour normaliser les vecteurs
E_norm = np.sqrt(Ex**2 + Ey**2)

# Pour éviter les divisions par zéro
E_norm[E_norm == 0] = 1e-5
Ex_unit = Ex / E_norm
Ey_unit = Ey / E_norm

# Paramètre d'affichage des flèches (adaptatives)
# Intervale des flèches
nb = 6 + N_dynodes//6

percentile_10th = np.percentile(E_norm, 10)
percentile_90th = np.percentile(E_norm, 90)
colors = np.clip(E_norm, a_min=percentile_10th, a_max=percentile_90th)

# Paramètre graphique
plt.quiver(X[::nb, ::nb], Y[::nb, ::nb], Ex_unit[::nb, ::nb], Ey_unit[::nb, ::nb], colors[::nb, ::nb], cmap="plasma_r")
plt.title("Champ électrique dans le tube PM")
plt.colorbar(label='Champs Électrique (V/m)', location='bottom')

plt.axis("equal")
 
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.show()


#=============================
# Graphique Champs + Potentiel
#=============================

# Affichage du potentiel (fond pâle)
plt.imshow(V_final, origin='lower', cmap='plasma', extent=[0, longueur, 0, hauteur], alpha=0.5)
plt.colorbar(label='Potentiel (V)', location='bottom', shrink=0.8, aspect=20)

# Champ électrique par-dessus
plt.quiver(X[::nb, ::nb], Y[::nb, ::nb], Ex_unit[::nb, ::nb], Ey_unit[::nb, ::nb], colors[::nb, ::nb], cmap="viridis_r")
plt.colorbar(label="Champ Électrique (V/m)", location='bottom', shrink=0.8, aspect=20)

# Axes et titre
plt.title("Champ électrique superposé au potentiel")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")

plt.show()




"""
==============================
Calcul en lien avec l'électron
==============================

Force sur l'électron dans un champs E
F = qE(x, y)

2e loi de newton
F = ma
(d"x/dt") = qE_x/m
(d"y/dt") = qE_y/m

 --- constantes physiques ---
q = -1.6022e-19 Coulombs
m =  9.1094e-31 kg

Utiliser la méthode d'euleur
-----------------------------
Déterminer la position x(t)
Condition initiale de x(t=0) et v(t=0)

Conditions initiales
--------------------
x = 0 
y = 0 (Selon mes axes cela correspond à y = 3)
v_x = 0
v_y = 0
"""

#=========================
#Trajectoire de l'électron
#=========================

# Direction du rebond sur la dynode
# Dictionnaire {dynode#: y + 2 ou y - 2}
bounce = {}

for i in range(1, N_dynodes+1):
  div = i % 2

  if div == 0:
    bounce[i] = -2

  else:
    bounce[i] = 2

print(bounce)
  

def euler_electron_2D(Ex, Ey, r_init, v_init):
  """
  Intègre la trajectoire de l'électron dans le tube PM.
  Lorsqu'il y a collision, l'électron rebondit verticalement de 2 mm 
  (la position y de la position est modifiée de ±2 mm et v_y change de direction).
        
  Paramètres:
  - E: champ électrique
  - r_init: vecteur de la position initiale (x, y)
  - v_init: vitesse initiale (v_x, v_y)
  - t: temps
  - n: nombre d'itérations
  - store: intervalle pour stocker les positions
  - dynodes: liste de dictionnaires définissant les zones de dynode et le sens du rebond
        
  Retourne:
  - position: Matrice des positions
  """
  q = -1.6022e-19 
  m =  9.1094e-31
