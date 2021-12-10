data = open("input.txt", "r").readlines()

m = len(data)
n = len(data[0]-1)
low_points = []

print(m)
print(n)

for x in range(0,m):
    for y in range(0,n):
        print(data[x][y])
        val = int(data[x][y])
        neighbors = []
        if x == 0 and y == 0:
            neighbors = [data[x+1][y], data[x][y+1]]
        elif x == 0 and y == n-1:
            neighbors = [data[x+1][y], data[x][y-1]]
        elif y == 0 and x == m-1:
            neighbors = [data[x][y+1], data[x-1][y],data[x][y+1]]
        elif y == n-1 and x == m-1:
             neighbors = [data[x-1][y], data[x][y-1]]
        elif x == 0:
            neighbors = [data[x+1][y], data[x][y-1], data[x][y+1]]
        elif y == 0:
             neighbors = [data[x][y+1], data[x-1][y], data[x+1][y]]
        elif y == n-1:
            neighbors = [data[x-1][y], data[x+1][y], data[x][y-1]]
        elif x == m-1:
            neighbors = [data[x][y+1], data[x][y-1], data[x-1][y]]
        else:
            neighbors = [data[x-1][y], data[x+1][y], data[x][y-1], data[x][y+1]]

        neighbors = [int(i) for i in neighbors]
    
        print(neighbors)
   
        if val < min(neighbors):
            low_points.append(val+1)

print(low_points)

print(f"The answer to part 1 is {sum(low_points)}")