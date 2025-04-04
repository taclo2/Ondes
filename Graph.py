import numpy as np
import matplotlib.pyplot as plt

# Dimensions in meters
L = 0.75 - 0.0254
M = 0.75 - 0.0254

# Frequency in Hz
omega = 7 * np.pi / M

# Time
t_fixed = 4

# Other parameters
damping_adjustment = 0.02
v = 0.5
s0 = 0.01

# Grid for x and y
x = np.linspace(0, L, 25)
y = np.linspace(0, M, 25)
X, Y = np.meshgrid(x, y)

# Calculate the solution over the grid
Z = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        Z[j, i] = analytical_solution(X[j, i], Y[j, i], t_fixed, damping_adjustment, v, s0, L, M, omega)

# Plotting as a contour plot
plt.figure(facecolor='black')
plt.contourf(X, Y, Z, levels=50, cmap='viridis', linewidths=3)
plt.xlabel("X axis", color='white')
plt.ylabel("Y axis", color='white')
plt.title("Analytical Solution at t = {:.2f}".format(t_fixed), color='white')
plt.gca().spines[:].set_color('white')
plt.tick_params(colors='white')
plt.show()

def analytical_solution(x, y, t, gamma, v, s0, L, M, omega):
    sum_result = 0
    n_range = 10  # Number of terms in the summation for n
    m_range = 10  # Number of terms in the summation for m
    
    for n in range(1, n_range+1):
        for m in range(1, m_range+1):
            n_pi_L = n * np.pi / L
            m_pi_M = m * np.pi / M
            
            lambda2 = n_pi_L**2 + m_pi_M**2
            gamma2 = gamma**2 + v**2 * lambda2
            beta = (np.cos(m * np.pi / 2) * np.cos(lambda2 * M / 2)) / (lambda2 * v**2 + gamma**2 * v**2)
            
            integral = (2 * tau) * np.sin(n * np.pi * x / L) * np.sin(m * np.pi * y / M) * np.exp(-gamma2 * t) * np.exp(-gamma2 * 2 * tau)
            sum_result += integral / (L * M)
    
    return sum_result