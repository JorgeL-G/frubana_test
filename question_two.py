#!/bin/python3

import os
import sys

""" Clase de Python
clase para la creación y funcionalidades basicas de un grafo.
graph = { 1 : [2],
          2 : [1,4],
          3 : [1,2,4],
          4 : []
        }
"""
class Graph(object):

    def __init__(self, graph_dict=None):
        'Función para la inicializar un grafo, si no se da un grafo, se inicializa en vacio'
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def add_vertex(self, vertex):
        'Función para agregar un nodo al grafo'
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        'Función para agregar un arco al grafo'
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            self.__graph_dict[vertex2] = [vertex1]

    def find_path(self, start_vertex, end_vertex, path=None):
            'Función que encuentra un camino entre un nodo A y B'
            if path == None:
                path = []
            graph = self.__graph_dict
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return path
            if start_vertex not in graph:
                return None
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_path = self.find_path(vertex, end_vertex, path)
                    if extended_path:
                        return extended_path
            return None


def find_cost(path, c):
    'Función que encuentra el costo para un camino'
    cost = 0
    colors_traveled = list()
    for vertex in path:
        if not c[vertex-1] in colors_traveled:
            cost += 1
            colors_traveled.append(c[vertex-1])

    return cost


def solve(c, tree):
    'Función que crea y recorre el grafo para saber el costo de los caminos'
    # Inicializamos la variable con la estructura de un grafo y matriz
    graph = Graph()
    matrix = list()
    # Agregamos todos los nodos
    for x in range(1, len(c)+1):
        graph.add_vertex(x)
        matrix.append([0] * len(c))
    # Agregamos todos los vertices
    for edge in tree:
        graph.add_edge(edge)

    # Se crea una matriz de costo d(i,j), siendo i y j nodos del grafo, se recorre la matriz superior
    for x in range(0, len(c)):
        for y in range(x, len(c)):
            if x == y:
                matrix[x][y] = 1
            else:
                path = graph.find_path(x+1, y+1)
                cost = find_cost(path, c)
                matrix[x][y] = matrix [y][x] = cost

    result = list()
    for cost in matrix:
        result.append(sum(cost))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    c = list(map(int, input().rstrip().split()))
    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    result = solve(c, tree)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
