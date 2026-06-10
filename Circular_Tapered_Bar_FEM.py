import numpy as np
import math

# ==================================
# INPUT DATA
# ==================================
L = float(input("Enter length L: "))
P = float(input("Enter load P: "))
d1 = float(input("Enter diameter d1: "))
d2 = float(input("Enter diameter d2: "))
E = float(input("Enter Young's Modulus E: "))
n = int(input("Enter number of elements n: "))

# ==================================
# ELEMENT LENGTH
# ==================================
le = L / n
nnodes = n + 1

# ==================================
# GLOBAL STIFFNESS MATRIX
# ==================================
K = np.zeros((nnodes, nnodes))

# ==================================
# ASSEMBLY PROCESS
# ==================================
for e in range(n):

    # Midpoint coordinate of element
    x_mid = (e + 0.5) * le

    # Diameter at midpoint
    d_mid = d1 + ((d2 - d1) / L) * x_mid

    # Area at midpoint
    A = (math.pi / 4) * d_mid**2

    # Element stiffness matrix
    ke = (E * A / le) * np.array([[1, -1],
                                  [-1, 1]])

    # Assembly into global matrix
    K[e:e+2, e:e+2] += ke

# ==================================
# LOAD VECTOR
# ==================================
F = np.zeros(nnodes)
F[-1] = P

# ==================================
# APPLY BOUNDARY CONDITION
# Node 1 fixed (u1 = 0)
# ==================================
K_reduced = K[1:, 1:]
F_reduced = F[1:]

# ==================================
# SOLVE DISPLACEMENTS
# ==================================
u_unknown = np.linalg.solve(K_reduced, F_reduced)

U = np.zeros(nnodes)
U[1:] = u_unknown

# ==================================
# ANALYTICAL DISPLACEMENT
# ==================================
u_exact = (4 * P * L) / (math.pi * E * d1 * d2)

# ==================================
# OUTPUT
# ==================================
print("\\nGlobal Stiffness Matrix:")
print(K)

print("\\nNodal Displacements:")
for i in range(nnodes):
    print(f"Node {i+1}: {U[i]:.8f}")

print("\\nFree End Displacement (FEM):", U[-1])
print("Analytical Displacement:", u_exact)

error = abs((u_exact - U[-1]) / u_exact) * 100
print("Percentage Error:", error, "%")
