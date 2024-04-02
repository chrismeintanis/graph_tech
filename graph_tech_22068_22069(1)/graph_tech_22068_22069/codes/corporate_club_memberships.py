import networkx as nx
import algorithm_networkx as anx

file_path = "C:/Users/user/Downloads/download.tsv.brunson_club-membership/brunson_club-membership/out.brunson_club-membership_club-membership"

# Διαβάστε το αρχείο και δημιουργήστε το γράφο
G = nx.read_edgelist(file_path)

# Παράμετροι για την συνάρτηση compute_Z_networkx
r = 3
c = 0.1
iterations = 100
tolerance = 1e-4

# Κλήση της συνάρτησης `compute_Z_networkx` με τον γράφο G που δημιουργήθηκε
result_Z = anx.compute_Z_networkx(G, r, c, iterations, tolerance)
print(result_Z)
print("Ο αλγόριθμος ολοκληρώθηκε με επιτυχία.")

