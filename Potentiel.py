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

#Paramètre du Graphique
# Point d'observation
r_max = 2
z_max = 10
M = 41
r_cyl = np.linspace(r_max/M, r_max, M)
z = np.linspace(-z_max/2, z_max/2, M)
R,Z = np.meshgrid(r_cyl, z)

V_ligne = R*0

# Ligne de charge
q_total = 1

L = 4        # Grandeur de la ligne
N = 101        # Nombre de sources discrètes sur la ligne
Z_prime = np.linspace(-L/2, L/2, N, endpoint=False )
dz_prime = Z_prime[1] - Z_prime[0]

densite_charge = q_total/L
dq = densite_charge * dz_prime

# Pour simplifier, je suppose que 1/(4 pi epsilon_o) = 1
for z_prime in Z_prime:
  r = np.sqrt((Z-z_prime)*(Z-z_prime)+R*R)
  V_ligne += -dq/r

dVdz = np.zeros(V_ligne.shape)
for i in range(1,V_ligne.shape[0]-1):
  for j in range(V_ligne.shape[1]):
    dz = Z[i+1,j]-Z[i-1,j]
    dV = (V_ligne[i+1,j]-V_ligne[i-1,j])
    dVdz[i,j] = dV/dz

dVdr = np.zeros(V_ligne.shape)
for i in range(1,V_ligne.shape[0]-1):
  for j in range(1, V_ligne.shape[1]-1):
    dr = R[i,j+1]-R[i,j-1]
    dV = (V_ligne[i,j+1]-V_ligne[i,j-1])
    dVdr[i,j] = dV/dr

lengths = np.sqrt(dVdz*dVdz + dVdr*dVdr)
percentile_10th = np.percentile(lengths, 10)
percentile_90th = np.percentile(lengths, 90)
colors = np.clip(lengths, a_min=percentile_10th, a_max=percentile_90th)

plt.contourf(R, Z, V_ligne, cmap = 'viridis_r')
plt.title("Potentiel")
plt.colorbar()
plt.show()