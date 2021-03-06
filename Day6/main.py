data = open("input.txt", "r").readlines()[0]

lantern_fishes = [int(i) for i in data.split(",")]

lantern_fishes_count = [lantern_fishes.count(i) for i in range(0,9)]

def count_fished_exp(count_list, days=80):
    for day in range(0, days):
        old = count_list.copy()
        for index, count in enumerate(count_list):
            count_list[index] = old[(index+1) % 9]

        count_list[6] = count_list[6] + old[0]    

    return sum(count_list)


print(f"The answer to part 1 is {(count_fished_exp(lantern_fishes_count.copy(), 80))}")

print(f"The answer to part 2 is {(count_fished_exp(lantern_fishes_count.copy(), 256))}")
