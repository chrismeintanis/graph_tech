import numpy as np

def compute_Z(MatrixY, r, c, iterations=100, tolerance=1e-4):
    n, _ = MatrixY.shape
    Z_prime = np.random.rand(n, r)
    t = 1

    while t <= iterations:
        Z = Z_prime.copy()

        for i in range(n):
            for j in range(n):
                Z[i] += c * (MatrixY[i, j] - np.dot(Z[i], Z[j])) * Z[j]

        if np.linalg.norm(Z - Z_prime, 'fro') < tolerance:
            break

        t += 1
        Z_prime = Z

    return Z