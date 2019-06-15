#!/bin/python3

import os
import sys

def unique_color_sum(root, edges, colors, size):
    node_colors = [set() for _ in range(size)]
    node_colors[root].add(colors[root])
    visited = set()
    visited.add(root)
    queue = [root]
    while queue:
        node = queue.pop(0)
        for x in edges[node]:
            if x not in visited:
                node_colors[x].update(node_colors[node])
                node_colors[x].add(colors[x])
                queue.append(x)
                visited.add(x)
    color_sum = 0
    for s in node_colors:
        color_sum += len(s)
    return color_sum

n = int(input())
colors = list(map(int, input().split()))
tree_graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    tree_graph[a].append(b)
    tree_graph[b].append(a)

for node in range(n):
    print(unique_color_sum(node, tree_graph, colors, n))