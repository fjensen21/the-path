# Implementation of BFS
# Features
    # Confirm if it is possible to get from node A -> B
    # Find the path with fewest segements from node A -> B
# Notes:
    # Directed graph: Edges are 1 way
    # Undirected graph: Edges go both ways
# Time Complexity: O(V+E)
    # Where V is the nmber of nodes (vertices); E is the number of edges
    # Must traverse every edge in the worst case and add every node to the queue
# Space Complexity: O(n) (storing every node in the queue and visited list)
from collections import deque


def get_morning_routine():
    routine = {
        "wake up": ["shower", "brush teeth"],
        "shower": [],
        "brush teeth": ["eat breakfast"],
        "eat breakfast": []
    }
    return routine

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while len(queue) > 0:
        current_node = queue.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbor in graph[current_node]:
                queue.appendleft(neighbor)
    return visited

if __name__ == "__main__":
    routine = get_morning_routine()
    start_node = "wake up"
    print(bfs(routine, start_node))
        