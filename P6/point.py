class Point:

    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.isOrigin = False

    def setIsOrigin(self):
        self.isOrigin = True
        self.nearestPoint = self.id
        self.distance = 0

    def findNearest(self, grid):
        if self.isOrigin:
            return self
        else:
            found = False
            step = 1
            while not found:
                origins = []
                neighbors = self.getNthNeighbors(step, grid)
                for neighbor in neighbors:
                    if neighbor.isOrigin:
                        origins.append(neighbor.id)
                if len(origins) > 1:
                    self.nearestPoint = "."
                    found = True
                    self.distance = step
                elif len(origins) == 1:
                    self.nearestPoint = origins[0]
                    found = True
                    self.distance = step
                step += 1
    def getNthNeighbors(self,n, grid):
        combinations = [(0, n)]
        for i in range(1, n):
            if n-i>0:
                combinations.append((i, n-i))
        neighbors = []
        for x, y in combinations:
            neighbors.append(grid.getPointByCoordinates(self.x+x, self.y+y))
            neighbors.append(grid.getPointByCoordinates(self.x-x, self.y+y))
            neighbors.append(grid.getPointByCoordinates(self.x+x, self.y-y))
            neighbors.append(grid.getPointByCoordinates(self.x-x, self.y-y))
        neighbors = [p for p in neighbors if p is not None]
        return set(neighbors)