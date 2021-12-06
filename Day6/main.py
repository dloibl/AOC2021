data = open("input.txt", "r").readlines()[0]

lantern_fishes = [int(i) for i in data.split(",")]


def calc_next_iteration(list):
    number_fishes = len(list)
    for index in range(0, number_fishes):
        fish_timer = list[index]
        if fish_timer == 0:
            list.append(8)
        list[index] = 6 if fish_timer == 0 else fish_timer-1

    return list


def count_fished_exp(population, for_day=80):
    for day in range(0, for_day - (for_day % 7), 7):
        new_borns = [(i+2) % 9 for i in population if i < 7]
        population = [i % 7 for i in population]
        population.extend(new_borns)

    for day in range(0, for_day % 7):
        population = calc_next_iteration(population)

    return population


print(f"The answer to part 1 is {len(count_fished_exp(lantern_fishes, 80))}")

print(len(count_fished_exp(lantern_fishes, 256)))
