def similar(s1, s2):
    differences = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            differences += 1
    return differences == 1

def common_chars(s1, s2):
    common = ""
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            common += c1
    return common

def main():
    with open("input.txt") as f1:
        for line1 in f1:
            with open("input.txt") as f2:
                for line2 in f2:
                    if similar(line1, line2):
                        print "Similar ids: %s and %s, common characters: %s" % (
                        line1, line2, common_chars(line1, line2))
                        return

if __name__ == '__main__':
    main()
