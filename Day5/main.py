import re

data = open("input.txt", "r").readlines()


def parse(data, all=False):
    lines = []
    maxVal = 0
    for line in data:
        m = re.search("(\d+),(\d+) -> (\d+),(\d+)", line)
        (x1, y1, x2, y2) = (int(m.group(1)), int(
            m.group(2)), int(m.group(3)), int(m.group(4)))
        if(all == True or (x1 == x2 or y1 == y2)):
            lines.append((x1, y1, x2, y2))
            maxVal = max([maxVal, x1, y1, x2, y2])
    grid = [[0 for _ in range(maxVal+1)] for _ in range(maxVal+1)]
    return (lines, grid)


(lines, grid) = parse(data)


def match_direction(v, p):
    d = diff(v[:2], v[2:])
    dp = diff(v[:2], p)
    if v[:2] == p or v[2:] == p:
        return True
    return d == dp


def diff(a, b):
    d = [b[0]-a[0], b[1]-a[1]]
    l = max(abs(d[0]), abs(d[1]))
    if l == 0:
        return [0, 0]
    return [int(d[0]/l), int(d[1]/l)]


def count_number_intersection(lines, grid):
    for line in lines:
        (x1, y1, x2, y2) = line
        for px in range(min(x1, x2), max(x1, x2)+1):
            for py in range(min(y1, y2), max(y1, y2)+1):
                if match_direction([x1, y1, x2, y2], [px, py]):
                    grid[py][px] += 1

    return sum([sum([1 if grid[i][j] > 1 else 0 for j in range(len(grid))])
                for i in range(len(grid))])


print(f"The answer to part 1 is", count_number_intersection(lines, grid))

(lines, grid) = parse(data, all=True)
print(f"The answer to part 2 is", count_number_intersection(lines, grid))

# for x in grid:
#     print("")
#     for y in x:
#         print(y if y >= 1 else ".", end="")
