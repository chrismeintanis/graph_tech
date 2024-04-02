import networkx as nx
import numpy as np

def compute_Z_networkx(G, r, c, iterations=100, tolerance=1e-4):
    n = len(G.nodes)
    Z_prime = np.random.rand(n, r)
    t = 1

    while t <= iterations:
        Z = Z_prime.copy()

        for i in range(n):
            for j in range(n):
                if G.has_edge(i, j):
                    Z[i] += c * (G[i][j]['weight'] - np.dot(Z[i], Z[j])) * Z[j]

        if np.linalg.norm(Z - Z_prime, 'fro') < tolerance:
            break

        t += 1
        Z_prime = Z

    return Z