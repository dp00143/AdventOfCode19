def twice(s):
    char_dict = {c: 0 for c in s}
    for c in s:
        char_dict[c] += 1
    return any(i == 2 for i in char_dict.values())


def thrice(s):
    char_dict = {c: 0 for c in s}
    for c in s:
        char_dict[c] += 1
    return any(i == 3 for i in char_dict.values())


if __name__ == '__main__':
    with open("input.txt") as f:
        doubles = 0
        triplets = 0
        for line in f:
            if twice(line):
                doubles += 1
            if thrice(line):
                triplets += 1
        print "Checksum: %i * %i = %i" % (doubles, triplets, doubles * triplets)
