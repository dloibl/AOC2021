data = open("input.txt", "r").readlines()

graph = {}

for edge in data:
    e = edge.split("-")
    from = e[0]
    to = e[1]
    if node[from] is None:
        graph[from] = [to]
    else:
        graph[from].append(to)

print(graph)

visited = set()

def is_small(cave):
    return cave == cave.lower()

def traverse(visited, graph, cave, count):
    if cave == "end":
        count += 1
    if is_small(cave) and not cave in visited:
        visited.add(cave)
        print("visited",visited)
        for neighbour in graph[cave]:
            traverse(visited, graph, neighbour, count)
    if not is_small(cave):
        for neighbour in graph[cave]:
            traverse(visited, graph, neighbour, count)
    return count        


print(traverse(visited, graph, "start", 0))       