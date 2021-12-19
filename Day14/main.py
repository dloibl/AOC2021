data = open("input.txt", "r").readlines()

polymer = data[0]

pair_insertion = {}
for line in data[2:]:
    [token, replacement] = line.strip().split(" -> ")
    pair_insertion[token] = replacement


result = [i for i in polymer.strip()]
for step in range(0, 10):
    next = []
    for i, si in enumerate(result):
        if i < len(result)-1:
            next.append(si)
            next.append(pair_insertion[result[i]+result[i+1]])
        else:
            next.append(si)

    result = next

count = [result.count(a) for a in set(pair_insertion.values())]

print("The answer of part 1 is", max(count) - min(count))
