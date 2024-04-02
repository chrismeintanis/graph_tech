import networkx as nx
import community
import matplotlib.pyplot as plt

def plot_partitioned_graph(G, partition):
    pos = nx.spring_layout(G)  # Ορίζουμε τη θέση των κόμβων για τον γράφο
    cmap = plt.get_cmap("viridis")
    colors = [cmap(partition[node] / max(partition.values())) for node in G.nodes]

    nx.draw(G, pos, node_color=colors, with_labels=True, font_weight='bold')
    plt.show()

def louvain_graph_partitioning(G):
    partition = community.best_partition(G)
    return partition

file_path = "C:/Users/user/Downloads/download.tsv.moreno_zebra/moreno_zebra/out.moreno_zebra_zebra"

G = nx.read_edgelist(file_path)

# Εφαρμογή του αλγορίθμου γραφικής διαίρεσης
partition = louvain_graph_partitioning(G)

# Εκτύπωση των κοινοτήτων
communities = {}
for node, community_id in partition.items():
    if community_id not in communities:
        communities[community_id] = []
    communities[community_id].append(node)

for community_id, nodes in communities.items():
    print(f"Community {community_id + 1}: {nodes}")

# Σχεδίαση του γράφου με βάση τις κοινότητες
plot_partitioned_graph(G, partition)