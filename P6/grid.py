from point import Point


class Grid:

    def __init__(self, n, m):
        self.x_max = n
        self.y_max = m
        self.points = {}
        for i in range(1, n+1):
            for j in range(1, m+1):
                pId = "Px%iy%i" % (i, j)
                self.points[pId] = Point(i, j, pId)

    def getPointById(self, pId):
        if pId in self.points:
            return self.points[pId]
        else:
            return None

    def getPointByCoordinates(self, x, y):
        pId = "Px%iy%i" % (x, y)
        return self.getPointById(pId)