#!/bin/python3

import os
import sys

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            self.__graph_dict[vertex2] = [vertex1]

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
            """ find a path from start_vertex to end_vertex
                in graph """
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
    cost = 0
    colors_traveled = list()
    for vertex in path:
        if not c[vertex-1] in colors_traveled:
            cost += 1
            colors_traveled.append(c[vertex-1])

    return cost


# Complete the solve function below.
def solve(c, tree):
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
