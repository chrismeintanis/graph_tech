import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import algorithm_networkx as anx

# Παράδειγμα 1: Γράφος με τρεις κόμβους
G1 = nx.Graph()
G1.add_nodes_from([0, 1, 2])
G1.add_edges_from([(0, 1, {'weight': 0.5}), (1, 2, {'weight': -1.0})])

# Παράδειγμα 2: Κατευθυνόμενος γράφος με τέσσερις κόμβους
G2 = nx.DiGraph()
G2.add_nodes_from([0, 1, 2, 3])
G2.add_edges_from([(0, 1, {'weight': 0.8}), (1, 2, {'weight': -0.2}), (2, 3, {'weight': 0.6})])

# Εκτύπωση των γράφων
plt.subplot(121)
nx.draw(G1, with_labels=True, font_weight='bold')
plt.title('Παράδειγμα 1')

plt.subplot(122)
nx.draw(G2, with_labels=True, font_weight='bold')
plt.title('Παράδειγμα 2')

plt.show()

# Εφαρμογή του αλγορίθμου σε κάθε γράφο
r_value = 2  # Τυχαία τιμή για το r
c_value = 0.1  # Τυχαία τιμή για το c

Z1 = anx.compute_Z_networkx(G1, r_value, c_value)
Z2 = anx.compute_Z_networkx(G2, r_value, c_value)

print("Πίνακας Z για το Παράδειγμα 1:")
print(Z1)

print("\nΠίνακας Z για το Παράδειγμα 2:")
print(Z2)

# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt

# Παράδειγμα 3: Σύνθετος γράφος με τέσσερις κόμβους και βάρη ακμών
G3 = nx.Graph()
G3.add_nodes_from([0, 1, 2, 3])
G3.add_edges_from([(0, 1, {'weight': 0.5}), (1, 2, {'weight': -1.0}), (2, 3, {'weight': 0.8}), (0, 3, {'weight': 0.2})])

# Παράδειγμα 4: Κατευθυνόμενος γράφος με πέντε κόμβους και βάρη ακμών
G4 = nx.DiGraph()
G4.add_nodes_from([0, 1, 2, 3, 4])
G4.add_edges_from([(0, 1, {'weight': 0.8}), (1, 2, {'weight': -0.2}), (2, 3, {'weight': 0.6}), (3, 4, {'weight': 0.4}), (4, 0, {'weight': -0.3})])

# Εκτύπωση των γράφων
plt.subplot(121)
nx.draw(G3, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray', width=2)
plt.title('Παράδειγμα 3')

plt.subplot(122)
nx.draw(G4, with_labels=True, font_weight='bold', node_color='lightcoral', edge_color='gray', width=2, arrowsize=20)
plt.title('Παράδειγμα 4')

plt.show()

# Εφαρμογή του αλγορίθμου σε κάθε γράφο
r_value = 3  # Τυχαία τιμή για το r
c_value = 0.15  # Τυχαία τιμή για το c

Z3 = anx.compute_Z_networkx(G3, r_value, c_value)
Z4 = anx.compute_Z_networkx(G4, r_value, c_value)

print("Πίνακας Z για το Παράδειγμα 3:")
print(Z3)

print("\nΠίνακας Z για το Παράδειγμα 4:")
print(Z4)