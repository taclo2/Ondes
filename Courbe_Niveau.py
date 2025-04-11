from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib as plt


def graphe(Z):
    n = Z.shape[0]
    X = Y = np.arange(n)

    fig = plt.figure(0, figsize=(10,8))
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                           cmap=cm.spectral_r, linewidth=0, antialiased=False)
    ax.set_zlim(-1, 1)
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.tight_layout()

    fig1 = plt.figure(1, figsize=(6, 6))
    cont = plt.contour(Z, np.arange(21)/10-1, cmap=cm.spectral_r)
    plt.clabel(cont, cont.levels, inline=True, fmt='%1.1f', fontsize=10)

    plt.xlabel('x')
    plt.ylabel('Y')
    plt.title('Courbes de niveau')
    plt.tight_layout()
    plt.show()
    


