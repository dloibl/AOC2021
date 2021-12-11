data = open("input.txt", "r").readlines()

octopuses = [[int(i) for i in line.strip()] for line in data]

m = len(data)


def flash(matrix, i, j, flashed):
    count = 0
    if matrix[i][j] > 9 and flashed[i][j] == False:
        flashed[i][j] = True
        count += 1
        for nx in [-1, 0, 1]:
            for ny in [-1, 0, 1]:
                if(i+nx >= 0 and j+ny >= 0 and i+nx < m and j+ny < m):
                    matrix[i+nx][j+ny] += 1
                    count += flash(matrix, i+nx, j+ny, flashed)

    return count


def step(matrix):
    matrix = [[i+1 for i in row] for row in matrix]

    flash_count = 0
    flashed = [[False for _ in row] for row in matrix]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            flash_count += flash(matrix, i, j, flashed)

    matrix = [[0 if i > 9 else i for i in row] for row in matrix]
    return (flash_count, matrix)


total = 0
for i in range(0, 100):
    (flash_count, octopuses) = step(octopuses)
    total += flash_count

print(f"The answer to part 1 is ", total)
