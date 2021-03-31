import networkx as nx
import numpy as np

np.seterr(divide='ignore', invalid='ignore')


def matrix_from_graph():
    G = nx.read_gml('remote.gml')
    A = nx.adjacency_matrix(G)
    # print(A)

    B = (A / A.sum(axis=0))
    B = np.nan_to_num(B, nan=0)

    # print(B)
    B.tofile('ttt.out',sep=' ')

    height, width = B.shape
    print(height,width)
    return B, height, width
    # print(B.shape)

    # print(type(B))
    # print(len(B[0]))

    # print(B)
    # pg = nx.pagerank(G)

    # G2 = nx.DiGraph(G)
    # eigen_centrality = nx.eigenvector_centrality(G2, max_iter=1000)
    #
    # print(eigen_centrality)
    # np.savetxt('array.out', B)


if __name__ == '__main__':
    matrix_from_graph()
