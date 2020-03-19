from grid import Grid
from pprint import pprint


def process_input(f):
    x_max = 0
    y_max = 0
    origins = []
    for line in f:
        x, y = line.split(', ')
        x, y = (int(x), int(y))
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
        origins.append((x, y))
    return origins, x_max, y_max


def main():
    with open("input.txt") as f:
        origins, x_max, y_max = process_input(f)
        print "Initialising grid"
        grid = Grid(x_max, y_max)
        print "Inserting origins"
        for x_origin, y_origin in origins:
            grid.getPointByCoordinates(x_origin, y_origin).setIsOrigin()
        print "Computing . . . . . "
        for l, point in enumerate(grid.points.values()):
            #print "Point %i (of %i)" % (l, len(grid.points.values()))
            point.findNearest(grid)
        area_count = {}

        print "Calculating Borders"
        excludes = []
        for y in range(1, y_max):
            excludePoint1 = grid.getPointByCoordinates(1, y).nearestPoint
            excludePoint2 = grid.getPointByCoordinates(x_max, y).nearestPoint
            excludes.extend([excludePoint1, excludePoint2])
        for x in range(1, x_max):
            excludePoint1 = grid.getPointByCoordinates(x, 1).nearestPoint
            excludePoint2 = grid.getPointByCoordinates(x, y_max).nearestPoint
            excludes.extend([excludePoint1, excludePoint2])
        #pprint(excludes)

        print "Counting area sizes"
        for point in grid.points.values():
            if point.nearestPoint not in excludes:
                if point.nearestPoint in area_count:
                    area_count[point.nearestPoint] += 1
                else:
                    area_count[point.nearestPoint] = 1

        pprint(area_count)
        #maxAreaId = max(area_count, key=lambda key: area_count[key] if key not in excludes else 0)
        #print "max area is %s with size %i" % (maxAreaId, area_count[maxAreaId])
if __name__ == '__main__':
    main()
