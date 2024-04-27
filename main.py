import networkx as nx
import matplotlib.pyplot as plt


def get_maximal_i_set(graph):
    x = set(graph.nodes())
    y = set()
    s = set()
    while len(x) != 0:
        u = x.pop()
        s.add(u)
        for v in graph.neighbors(u):
            x.discard(v)
            y.add(v)
    return s


def rlf(graph):
    v = set(graph.nodes())
    i = 1
    color = {}
    while len(v) != 0:
        maximal = get_maximal_i_set(graph)
        color[i] = maximal
        i += 1
        v -= maximal
        graph.remove_nodes_from(maximal)
    return color


def read_edge(filename):
    edge = []
    with open(filename, 'r') as file:
        for line in file:
            source, target = line.strip().split()
            source = int(source)
            target = int(target)
            edge.append((source, target))
    return edge


def main():
    file = input("Enter file path: ")
    edge_list = read_edge(file)
    g = nx.Graph()
    g.add_edges_from(edge_list)
    g1 = g.copy()
    print("Number of nodes:", g.number_of_nodes())
    print("Number of edges:", g.number_of_edges())
    colormap = rlf(g1)
    print(colormap)

    color = [None] * 12

    for i in colormap.keys():
        for j in colormap[i]:
            color[j] = i

    print(color)

    nx.draw(g, node_color=color, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    main()
