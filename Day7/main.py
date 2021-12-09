import operator

data = open("input.txt", "r").readline()

crabs_pos = [int(i) for i in data.split(",")]
crabs_count = len(crabs_pos)


def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


min_index, fuel = min(enumerate([manhattan(crabs_pos, [m for _ in range(0, crabs_count)])
                                for m in range(0, crabs_count)]), key=operator.itemgetter(1))

print(
    f"The answer to part 1 is {crabs_pos[min_index]} with total fuel use {fuel}")
