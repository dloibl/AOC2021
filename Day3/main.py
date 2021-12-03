data = open("input.txt", "r").readlines()

size = len(data[0])-1
result = [0] * size

for value in data:
    for index, bit in enumerate(value):
        if(index < size):
            result[index] += 1 if int(bit) == 1 else -1

gamma_rate = int("".join(["0" if x < 0 else "1" for x in result]), 2)
epsilon_rate = int("".join(["1" if x < 0 else "0" for x in result]), 2)

print(f"The answer to part 1 is {gamma_rate*epsilon_rate}")
