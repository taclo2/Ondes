import matplotlib.pyplot as plt
import numpy as np

"""
====================================
Fonctions principales de Matplotlib
====================================

Tracer une courbe de y en fonction de x avec le style styleDuGraphe
Le nom de la coyrbe s'affiche dans la légende (label)
plt.plot(x, y, styleDuGraphe, linewidth=1, label = "y = f(x)")


plt.xlabel("x - axe des abscisses")
plt.ylabel("y - axe des ordonnées")

Pour définir des valeurs min et max 
plt.axis([-5.5, 5.5, 0, 10])

ou
plt.xlim(-5.5, 5.5)
plt.ylim(0, 10)


Ajouter un titre au graphique et ajouter une grille
plt.title("y en fonction de x")
plt.grid()


Tracer une vecteur au point d'application (xVecteur, yVecteur)
vecteurX composante suivant x, vecteurY composante suiavnt y
vecteur = plt.quiver(xVecteur, yVecteur, vecteurX, vecteurY, 
                    scale=echelleVecteur, colcor='r', angle='xy', units='xy')

                    
Trace l'échelle correspondant au vecteur vecteur, en position (0.1, 0.1)
plt.quiverkey(vecteur, 0.1, 0.1, 2, label='échelle 2 m/s', coordinates='data')


Afficher une legende avec le nom des courbes
plt.legend()

Afficher le graph
plt.show()

"""



#=====================
#Exemple 1 : graph 1D
#=====================

"""
Pour représenter le graphe d'une fonction réelle f définie sur un intervalle [a, b],
on commence par construire un vecteur X, discrétisant l'intervalle [a, b], en considérant un ensemble
de points équidistants dans [a, b].

Pour ce faire, on se donne un naturel N grand et on considère
X=numpy.linspace(a,b,N)

on considère
X=numpy.arange(a,b+h,h)
"""
x = np.linspace(0., 2*np.pi, 100)
plt.plot(x, np.exp(x/2)*np.cos(5*x), "-ro") #ro pour points rouges
plt.title("Fonction $f(x)=e^{x/2} cos(5x)$")
plt.xlabel("$x$")
plt.text(1, 15, "Courbe", fontsize=22)
plt.show()



#===========================
#Exemple 2: Tracer un carré
#===========================
"""
Coordonnées des sommets : X = (-1; 1; 1; -1; -1) et Y = (-1; -1; 1; 1; -1)
"""
X=np.array([-1, 1, 1,-1,-1])
Y=np.array([-1, -1, 1,1,-1])
plt.plot(X,Y,"r",lw=3)
plt.axis("equal")

plt.axis([-2,2,-2,2])
plt.title("Carre de cote 2")
plt.show()



#=============================
#Exemple 3: Plusieurs courbes
#=============================
"""
On peut superposer plusieurs courbes dans le même graphique
"""
X = np.linspace(0, 2*np.pi, 100)
y1 = np.cos(X)
y2 = np.sin(X)

# Tracé
plt.plot(X, y1, 'b', label='cos(x)')  # courbe bleue pour cos(x)
plt.plot(X, y2, 'r', label='sin(x)')  # courbe rouge pour sin(x)

# Ajouter la légende
plt.legend()

# Nom de l'axe des abscisses
plt.xlabel('$x$')  # le $...$ permet l’écriture mathématique avec LaTeX

plt.show()


#====================
#Exemple 4 : Meshgrid
#====================

x = np.array([3, 4, 7])
y = np.array([-1, 0])
X, Y = np.meshgrid(x, y)

"""
X
array([[3, 4, 7],
       [3, 4, 7]])

Y
array([[-1, -1, -1],
       [ 0,  0,  0]])
"""