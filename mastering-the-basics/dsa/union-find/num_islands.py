class UnionFind:
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    cell_key = row * cols + col
                    self.parent.append(cell_key)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_x, node_y):
        root_x = self.find(node_x)
        root_y = self.find(node_y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1


def num_islands(grid):
    union_find = UnionFind(grid)
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                grid[row][col] = "0"

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if c in range(cols) and r in range(rows) and grid[r][c] == "1":
                        cell = row * cols + col
                        nei_cell = r * cols + c
                        union_find.union(cell, nei_cell)
    return union_find.count