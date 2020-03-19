def print_frequency(current, sign, change, result):
    s = "Current frequency  %i, change of %s%i; resulting frequency  %i."\
        % (current, sign, change, result)
    print s


if __name__ == '__main__':
    with open("input.txt") as f:
        current = 0
        for line in f:
            sign = line[0]
            change = int(line[1:])
            if sign == "+":
                result = current + change
            else:
                assert (sign == "-"), "Unsupported sign for change"
                result = current - change
            print_frequency(current, sign, change, result)
            current = result
        print "Final result: %i" % current


