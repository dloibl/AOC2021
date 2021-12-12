data = open("input.txt", "r").readlines()

graph = {}


for edge in data:
    [a, b] = edge.strip().split("-")
    if not a in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if not b in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)


visited = set()


def is_small(cave):
    return cave == cave.lower()


def traverse(visited, graph, cave, count, path):
    if is_small(cave):
        visited.add(cave)

    path.append(cave)

    if cave == "end":
        count += 1
    else:
        if cave in graph:
            for n in graph[cave]:
                if not is_small(n) or not n in visited:
                    count = traverse(visited, graph, n, count, path)

    path.pop()
    if cave in visited:
        visited.remove(cave)
    return count


print("The answer to part 1 is ", traverse(visited, graph, "start", 0, []))
