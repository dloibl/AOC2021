data = open("input.txt","r").readlines()

def count_increases(numbers):
    numbers_copy = numbers.copy()
    numbers_copy.pop(0)
    return sum([0 if int(a) - int(b) >= 0 else 1 for a, b in zip(numbers, numbers_copy)]) 

print(f"The answer to part 1 is {count_increases(data)}")

# part 2
data_copy = data.copy()
data_copy.pop(0)
data_copy_2 = data_copy.copy()
data_copy_2.pop(0)

sum_of_threes = [int(a) + int(b)+ int(c) for a, b, c in zip(data, data_copy, data_copy_2)]

print(f"The answer to part 2 is {count_increases(sum_of_threes)}")
