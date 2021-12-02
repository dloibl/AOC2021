data = open("input.txt","r").readlines()

dx = 0
dy = 0

for value in data:
    line = value.split(" ")
    direction = line[0]
    value = int(line[1].replace("\n",""))
    if direction == "down":
        dy=dy + value
    if direction == "up":
        dy=dy - value
    if direction == "forward":
        dx=dx + value

print(f"The answer to part 1 is {dx*dy}")

dx2 = 0
dy2 = 0
aim = 0

for value in data:
    line = value.split(" ")
    direction = line[0]
    value = int(line[1].replace("\n",""))
    if direction == "down":
        aim=aim + value
    if direction == "up":
        aim=aim - value
    if direction == "forward":
        dx2=dx2 + value
        dy2=dy2 + aim*value

print(f"The answer to part 2 is {dx2*dy2}")


