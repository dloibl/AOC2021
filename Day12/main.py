data = open("input.txt", "r").readlines()

graph = {}

for edge in data:
    [a,b] = edge.strip().split("-")
    if not a in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

print(graph)

visited = set()

def is_small(cave):
    return cave == cave.lower()

nr_path = 0

def traverse(visited, graph, cave):
    global nr_path
    if cave == "end":
        nr_path += 1
    if is_small(cave) and not cave in visited:
        visited.add(cave)
        print("visited",visited)
        if cave in graph:
            for neighbour in graph[cave]:
                traverse(visited, graph, neighbour)
    elif not is_small(cave) and cave in graph:
        for neighbour in graph[cave]:
            traverse(visited, graph, neighbour)     


traverse(visited, graph, "start")

print("The answer to part 1 is ", nr_path)