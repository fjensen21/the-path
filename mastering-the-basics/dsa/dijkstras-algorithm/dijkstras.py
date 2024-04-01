# Implementation of Dijkstra's Algorithm (Shortest Path Non Negative Edges)
# Features
    # Find the shortest path to a node through a weighted directed graph
# Time Complexity: 
# Space Complexity:

class WeightedGraphAM:
    def __init__(self):
        self.graph = []
        self.lookup = {}

    def add_node(self, name: str): 
        """Adds a node if doesn't already exist"""
        if name not in self.lookup:
            # Add node to lookup
            self.lookup[name] = len(self.graph)
            # Add space to graph for new node
            for row in self.graph:
                row.append(-1)
            self.graph.append([-1 for _ in range(len(self.graph)+1)])
    
    def add_edge(self, source, destination, weight):
        """Adds or overwrites and edge. Will add node if not already added"""
        self.add_node(source)
        self.add_node(destination)

        source_index = self.lookup[source]
        destination_index = self.lookup[destination]

        self.graph[source_index][destination_index] = weight
    
    def get_neighbors(self, node):
        """Given a node get its neighbors and return a list"""
        if node not in self.lookup:
            return []
        
        neighbors_row = self.graph[self.lookup[node]]
        neighbors = []
        for i in range(len(neighbors_row)):
            if neighbors_row[i] != -1:
                for key, value in self.lookup.items():
                    if value == i:
                        neighbors.append(key)
        
        return neighbors





def get_shortest_path_AM(graph: WeightedGraphAM, start_node: str, end_node: str):
    # Initialize costs with cost for start node neighbors and INF for other nodes
    pass



if __name__ == "__main__":
    graph = WeightedGraphAM()
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 3)
    graph.add_edge("A", "D", 4)
    graph.add_edge("D", "A", 4)
    graph.add_edge("D", "B", 4)
    pass