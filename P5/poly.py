from pprint import pprint
import string

def process_input(f):
    for line in f:
        return line

def react(polymer):
    last_unit = ''
    to_destroy = []
    for i, unit in enumerate(polymer):
        if unit != last_unit:
            if unit.lower() == last_unit.lower() and (i-1) not in to_destroy:
                to_destroy.extend([i-1, i])
        last_unit = unit
    to_keep = []
    for i in range(len(polymer)):
        if i not in to_destroy:
            to_keep.append(i)
    new_poly = ''
    #pprint(to_destroy)
    #print "###############################"
    #pprint(to_keep)
    #print "###############################"
    for i in to_keep:
        new_poly += polymer[i]
    return new_poly

def full_reaction(polymer):
    new_poly = react(polymer)
    while new_poly != polymer:
        polymer = new_poly
        new_poly = react(polymer)
    return polymer

def main():
    with open("input.txt") as f:
        polymer = process_input(f)
    length = len(polymer)
    for letter in string.ascii_lowercase:
        print letter
        shortened_polymer = polymer.replace(letter, "").replace(letter.upper(),"")
        after_reaction = full_reaction(shortened_polymer)
        if len(after_reaction)<length:
            shortest = after_reaction
            removed_letter = letter
            length = len(shortest)
    print "Shortest polymer:"
    print shortest
    print "Removed letter %s, resulting end length: %i" % (removed_letter, length)


if __name__ == '__main__':
    main()