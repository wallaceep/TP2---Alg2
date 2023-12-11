import networkx as nx
import pandas as pd
import sys
import time
from memory_profiler import memory_usage
import multiprocessing
import tsp_bnb
import christofides
import tat

timeLimit = 1

#Lê os datasets
def read_datasets(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def ler_dataset(nome_dataset):

    def convert_to_int(valor):  
        return int(float(valor))

    dataset_path = f'data/{nome_dataset}.tsp'
    graph = []

    with open(dataset_path, 'r') as file:
        lines = file.readlines()
        coord_section = False
        coords = {}

        for lines in lines:
            parts = lines.split()

            if len(parts) > 0:
                if parts[0] == 'NODE_COORD_SECTION':
                    coord_section = True
                elif parts[0] == 'EOF':
                    coord_section = False
                elif coord_section:
                    no, x, y = map(convert_to_int, parts)
                    coords[no] = (x, y)

    # Adicionar nós e arestas ao grafo
    for u, pos_u in coords.items():
        node_row = []
        for v, pos_v in coords.items():
            if u != v:
                distance = ((pos_u[0] - pos_v[0]) ** 2 + (pos_u[1] - pos_v[1]) ** 2) ** 0.5
                node_row.append(distance)
            else:
                node_row.append(0)
        graph.append(node_row)

    return graph

# Lê o arquivo com os datasets especificos do tp
tp_datasets = read_datasets('tp2_datasets.txt')
tp_datasets.pop(0)

# Escreve o arquivo de saída
def write_file(label, path, mode):
    with open(path, mode) as file:
        file.write(f'{label}\n')

# Calcula a distância  
def distance(cycle, matrix):
    total = 0
    for i in range(len(cycle) - 1):
        total += matrix[cycle[i]][cycle[i+1]]
    return total

alg = sys.argv[1].lower()

def wrapper_algoritmo_christofides(queue, G):
    result = christofides.christofides_tsp(G)
    queue.put(result)

if __name__ == "__main__":
    open("output_branch_and_bound.txt", 'w').close()
    open("output_christofides.txt", 'w').close()
    open("output_twice_around_tree.txt", 'w').close()

    for line in tp_datasets:
        dataset_name = line.split('\t')[0]
        graph = ler_dataset(dataset_name)
        adjacency_matrix = pd.DataFrame(graph)

        if (alg == "branch_and_bound"):
            print("rodando branch and bound")
            start_time = time.time()
            mem_before = memory_usage()[0]
            tsp_bab = tsp_bnb.branch_and_bound(len(graph))

            if (timeLimit):
                write_file(f"{dataset_name}, NaN", "output_christofides.txt", 'a')
            else:
                tsp_bab.TSP(graph)
                end_time = time.time()
                mem_after = memory_usage[0]
                
                elapsed_time = end_time - start_time
                memory = mem_after - mem_before
                euclidian_distance = tsp_bab.final_res()

                write_file(f"{dataset_name}, Distance: {euclidian_distance}, Memory: {memory}, Time: {elapsed_time}", "output_branch_and_bound.txt", 'a')
        
        if (alg == "christofides"):
            print("rodando christofides...")
            graph = nx.from_pandas_adjacency(adjacency_matrix)
            start_time = time.time()
            mem_before = memory_usage()[0]
            result_queue = multiprocessing.Queue()
            process = multiprocessing.Process(target=wrapper_algoritmo_christofides, args=(result_queue, graph))
            process.start()
            process.join(30*60)
            end_time = time.time()
            mem_after = memory_usage()[0]
            elapsed_time = end_time - start_time
            memory = mem_after - mem_before

            if not result_queue.empty():
                tour_result = result_queue.get()
                total_distance = distance(tour_result, graph)
                write_file(f"{dataset_name}, Distance: {total_distance}, Memory: {memory}, Time: {elapsed_time}", "output_christofides.txt" , 'a')
            else:
                write_file(f"{dataset_name}, Distance: {total_distance}, Memory: {memory}, Time: {elapsed_time}", "output_christofides.txt" , 'a')
        
        if (alg == "twice_around_the_tree"):
            graph = nx.from_pandas_adjacency(adjacency_matrix)

            if (timeLimit):
                write_file(f"{dataset_name}, NaN", "output_christofides.txt", 'a')  
            else:
                start_time = time.time()
                mem_before = memory_usage()[0]

                hamiltonian_cycle = tat.approx_tsp_tour(graph, 'weight')

                euclidian_distance = distance(hamiltonian_cycle, adjacency_matrix)

                end_time = time.time()
                mem_after = memory_usage()[0]
                
                elapsed_time = end_time - start_time
                memory = mem_after - mem_before
                
                write_file(f"{dataset_name}, Distance: {euclidian_distance}, Memory: {memory}, Time: {elapsed_time}", "output_twice_around_tree.txt" , 'a')