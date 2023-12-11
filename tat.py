import time
import networkx as nx
import math

max_execution_time = 1

class MaxExecTime(Exception):
    pass

def euclidean_distance(point1, point2):
    # Calculates the Euclidean distance between two points
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def approx_tsp_tour(G, positions):
    initial_exec_time = time.time()

    # Step 1: Select a vertex r in G.V to be a "root" vertex
    root = list(G.nodes())[0]

    # Step 2: Compute a minimum spanning tree T for G from root r using MST-Prim
    T = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')

    # Step 3: Let H be a list of vertices, ordered according to a preorder tree walk of T
    H = preorder_walk(T, root, initial_exec_time)

    # Step 4: Create a closed tour by repeating vertices in the preorder walk
    # closed_tour = H + [root]

    # Step 5: Calculate the total distance of the tour
    # total_distance = calculate_tour_distance(closed_tour, positions)

    # Step 6: Record execution time
    execution_time = time.time() - initial_exec_time

    # Step 7: Save results to output.txt
    # save_results(closed_tour, total_distance, execution_time)

    # Step 8: Return the Hamiltonian cycle
    return H

def calculate_tour_distance(tour, positions):
    # Calculate the total distance of the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    return total_distance

def save_results(tour, total_distance, execution_time):
    # Save results to output.txt
    with open("output.txt", "w") as file:
        file.write("Tour: {}\n".format(tour))
        file.write("Total Distance: {}\n".format(total_distance))
        file.write("Execution Time: {:.4f} seconds\n".format(execution_time))

def preorder_walk(tree, start_vertex, exec_start_time):
    """Realiza uma caminhada em pré-ordem na árvore.

    Args:
        tree (networkx.Graph): Uma árvore geradora mínima.
        start_vertex (node): O vértice inicial da caminhada.
        exec_start_time (float): O tempo de início da execução.

    Returns:
        list: Uma lista de vértices visitados durante a caminhada.
    """
    def depth_first_search(vertex, visited, start_time):
        visited.append(vertex)
        for neighbor in tree.neighbors(vertex):
            if neighbor not in visited:
                depth_first_search(neighbor, visited, start_time)

        return visited

    # Inicia a caminhada em pré-ordem
    visited_vertices = depth_first_search(start_vertex, [], exec_start_time)

    return visited_vertices