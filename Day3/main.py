data = open("input.txt", "r").readlines()

size = len(data[0])-1


def diagnostic(list=[], n=size):
    result = [0] * n
    for value in list:
        for index, bit in enumerate(value[0:n]):
            result[index] += 1 if int(bit) == 1 else -1
    return [[0 if x < 0 else 1 for x in result],  [1 if x < 0 else 0 for x in result]]


def decimal(bits=[]):
    return int("".join([str(x) for x in bits]), 2)


[gamma, epsilon] = diagnostic(list=data)

print(f"The answer to part 1 is {decimal(gamma)*decimal(epsilon)}")


def has_bit_value_at_pos(value=0, pos=0):
    return lambda bits: int(bits[pos]) == value


def life_support_rating(diagnostic_index=0, bits=[],  pos=0):
    if(len(bits) == 1 or pos >= size):
        return decimal(bits[0])
    result = diagnostic(bits)
    return life_support_rating(diagnostic_index,
                               list(filter(has_bit_value_at_pos(result[diagnostic_index][pos], pos), bits)), pos+1)


print(
    f"The answer to part 2 is {life_support_rating(0, data)*life_support_rating(1, data)}")
