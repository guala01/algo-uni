import csv
from collections import deque
import numpy as np

# csv importa come matrice di stringhe
def convert_str_matrix_to_int(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

# converto la matrice in numpy e la comparo con la sua trasposta se sono uguali il grafo sarà non orientato
def is_directed(matrix):
    matrix = np.array(matrix)
    if np.array_equal(matrix, matrix.T):
        return False
    else:
        return True


# implemento bfs usando deque come coda e la lista dei nodi visitati
# faccio un loop per ogni elemento della matrice
# controllo se c'e' un edge tra il nodo e nodo[i] e se e' stato visitato
def bfs(matrix, start):
    visited = [False]*len(matrix)
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if visited[node] is not True:
            print(f"Visitato nodo: {node}")
            visited[node] = True
            for i, is_edge in enumerate(matrix[node]):
                if is_edge and not visited[i]:
                    queue.append(i)
                  
# test
test_directed_matrix = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]


test_undirected_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

filename = 'graph.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    matrix = list(reader)

convert_str_matrix_to_int(matrix)

if is_directed(matrix):
    print("Grafo orientato.")
else:
    print("Grafo non orientato")

# chiamo bfs con il nodo di partenza desiderato
bfs(matrix, 0)