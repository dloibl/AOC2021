data = open("input.txt", "r").readlines()

score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def get_opening_bracket(bracket):
    if bracket == ")":
        return "("
    if bracket == "]":
        return "["
    if bracket == "}":
        return "{"
    if bracket == ">":
        return "<"


score = 0


def parse(line: str):
    stack = []
    for bracket in line.strip():
        if bracket in ["{", "(", "<", "["]:
            stack.append(bracket)
        else:
            last = stack.pop()
            expected = get_opening_bracket(bracket)
            if last != expected:
                print("corrupt expected", expected, " found ", bracket)
                return score_map[bracket]
    return 0


for line in data:
    score += parse(line)


print(f"The answer to part 1 is ", score)
