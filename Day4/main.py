data = open("input.txt", "r").readlines()

size = len(data[2].split())
numbers = data[0].strip().split(",")


class Board:
    def __init__(self, name):
        self.bingo = False
        self.name = name
        self.data = [[[None, False] for _ in range(size)] for _ in range(size)]

    def check_number(self, value):
        for x in range(size):
            for y in range(size):
                if self.data[x][y][0] == value:
                    self.data[x][y][1] = True

        vertical = [sum([1 if row[i][1] == True else 0 for i in range(0, len(row))])
                    for row in self.data]
        horizontal = [sum([1 if row[i][1] == True else 0 for row in self.data])
                      for i in range(0, len(self.data[0]))]

        if 5 in vertical or 5 in horizontal:
            self.bingo = True
            return True

        return False

    def sum_not_matched_numbers(self):
        sum_result = 0
        for x in range(size):
            for y in range(size):
                if self.data[x][y][1] == False:
                    sum_result += self.data[x][y][0]
        return sum_result

    def set_number(self, x, y, value):
        self.data[x][y][0] = value

    def print(self):
        print("\n")
        for y in range(size):
            print("\n")
            for x in range(size):
                if self.data[x][y][1] == False:
                    print(self.data[x][y][0], " ", end="")
                else:
                    print("X ", " ", end="")


def init_board(data):
    boards = []
    y = 0
    name = 1
    board = Board(name)
    for line in data[2:]:
        numbers = line.split()
        if(len(numbers) == 0):
            boards.append(board)
            name += 1
            board = Board(name)
            y = 0
        else:
            for x, value in enumerate(numbers, start=0):
                board.set_number(x, y, int(value))

            y += 1

    boards.append(board)
    return boards


def play(numbers, boards):
    for number in numbers:
        for board in boards:
            if board.check_number(int(number)) == True:
                print(f"The answer to part 1 is", (int(number) *
                      board.sum_not_matched_numbers()))
                return


boards = init_board(data)
play(numbers, boards)


def figure_out_which_board_wins_last(numbers, boards=[]):
    last_board = None
    last_number = None
    for number in numbers:
        for board in boards:
            if board.bingo:
                continue
            if board.check_number(int(number)) == True:
                last_board = board
                last_number = number

    print(f"The answer to part 2 is", (int(last_number) *
                                       last_board.sum_not_matched_numbers()))


figure_out_which_board_wins_last(numbers, boards)
