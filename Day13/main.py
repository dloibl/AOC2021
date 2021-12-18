data = open("input.txt", "r").readlines()

fold = []
points = []

for line in data:
    if len(line.strip()) == 0:
        continue
    elif line.startswith("fold"):
        [x_or_y, value] = line.replace("fold along ", "").split("=")
        fold.append((int(value) if x_or_y == "x" else 0,
                    int(value) if x_or_y == "y" else 0))
    else:
        [x, y] = line.split(",")
        points.append((int(x), int(y)))


def fold_paper(points, fold_points=[]):
    result = set(points)
    for f in fold_points:
        next_p = set()
        idx = 1 if f[0] == 0 else 0
        fp = f[idx]
        for p in result:
            if p[idx] < fp:
                next_p.add(p)
            if p[idx] > fp:
                next_p.add(
                    (2*fp - p[0] if idx == 0 else p[0],
                     2*fp - p[1] if idx == 1 else p[1])
                )

        result = next_p
    return result


r1 = fold_paper(points, fold[0:1])
print("The answer to part 1 is", len(r1))


def print_origami(result):
    for y in range(0, max([p[1] for p in result])+2):
        for x in range(0, max([p[0] for p in result])+2):
            if (x, y) in result:
                print("x", sep="", end="")
            else:
                print(".", sep="", end="")
        print("")


print("The answer to part 2 is")
result = fold_paper(points, fold)
print_origami(result)
