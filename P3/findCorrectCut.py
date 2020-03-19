def insert_cut(m, x, y, delta_x, delta_y):
    for i in range(x, x + delta_x):
        for j in range(y, y + delta_y):
            m[i][j] += 1


def insert_cut_id(m, id, x, y, delta_x, delta_y, overlaps):
    for i in range(y, y + delta_y):
        for j in range(x, x + delta_x):
            if m[i][j] == 0:
                m[i][j] = id
            else:
                overlaps.extend([m[i][j], id])


def count_overlapping(m):
    count = 0
    for a in m:
        for el in a:
            if el > 1:
                count += 1
    return count


def find_cut(ids, overlaps):
    for id in ids:
        if id not in overlaps:
            return id


if __name__ == '__main__':
    n = 1000;
    matrix = [[0 for x in range(n)] for y in range(n)]
    ids = []
    overlaps = []
    with open("input.txt") as f:
        for line in f:
            # Read params

            split = line.split(" ")
            id = split[0]
            start = split[2].strip(":").split(",")
            x_start = int(start[0])
            y_start = int(start[1])
            dimensions = split[3].split("x")
            x_dim = int(dimensions[0])
            y_dim = int(dimensions[1])

            # Insert cut
            insert_cut_id(matrix, id, x_start, y_start, x_dim, y_dim, overlaps)
            ids.append(id)
        print "Not overlapping cut id: %s, Total ids: %i, Overlapping ids: %i" % (find_cut(ids, overlaps), len(ids), len(set(overlaps)))