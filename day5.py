import re

directions = """move 6 from 1 to 7
move 2 from 2 to 4
move 2 from 7 to 4
move 6 from 4 to 3
move 1 from 5 to 1
move 3 from 8 to 3
move 15 from 3 to 4
move 6 from 5 to 9
move 14 from 4 to 2
move 3 from 2 to 7
move 1 from 2 to 7
move 9 from 9 to 1
move 3 from 2 to 1
move 7 from 6 to 7
move 1 from 6 to 8
move 2 from 9 to 1
move 9 from 2 to 3
move 8 from 3 to 9
move 1 from 1 to 4
move 1 from 8 to 6
move 1 from 6 to 2
move 5 from 9 to 8
move 2 from 9 to 1
move 1 from 4 to 2
move 17 from 1 to 9
move 1 from 3 to 1
move 3 from 2 to 3
move 2 from 4 to 5
move 12 from 7 to 3
move 16 from 9 to 2
move 5 from 7 to 5
move 2 from 1 to 2
move 1 from 3 to 6
move 1 from 4 to 6
move 1 from 7 to 3
move 1 from 6 to 3
move 7 from 3 to 4
move 5 from 8 to 3
move 1 from 6 to 7
move 7 from 3 to 4
move 6 from 3 to 1
move 2 from 4 to 8
move 1 from 5 to 2
move 10 from 4 to 5
move 3 from 5 to 2
move 2 from 8 to 9
move 5 from 2 to 8
move 1 from 3 to 5
move 2 from 5 to 8
move 12 from 5 to 7
move 1 from 4 to 2
move 5 from 9 to 4
move 1 from 2 to 5
move 6 from 1 to 3
move 6 from 3 to 5
move 10 from 7 to 4
move 2 from 7 to 3
move 4 from 7 to 6
move 1 from 9 to 5
move 12 from 2 to 1
move 1 from 8 to 7
move 3 from 7 to 4
move 4 from 4 to 8
move 7 from 5 to 3
move 1 from 2 to 4
move 10 from 1 to 5
move 2 from 1 to 2
move 4 from 6 to 7
move 8 from 8 to 3
move 5 from 4 to 9
move 12 from 3 to 8
move 4 from 3 to 8
move 2 from 9 to 2
move 3 from 5 to 4
move 1 from 3 to 5
move 1 from 7 to 6
move 14 from 4 to 6
move 6 from 5 to 9
move 8 from 2 to 8
move 3 from 5 to 7
move 21 from 8 to 4
move 16 from 4 to 9
move 8 from 6 to 2
move 4 from 6 to 1
move 1 from 4 to 6
move 2 from 4 to 8
move 3 from 1 to 8
move 2 from 4 to 6
move 1 from 6 to 2
move 3 from 8 to 4
move 2 from 2 to 5
move 2 from 5 to 7
move 1 from 8 to 9
move 1 from 4 to 9
move 1 from 1 to 6
move 3 from 6 to 3
move 3 from 2 to 3
move 1 from 4 to 6
move 3 from 6 to 7
move 10 from 9 to 7
move 1 from 4 to 7
move 6 from 8 to 3
move 1 from 6 to 8
move 2 from 2 to 5
move 1 from 2 to 1
move 1 from 8 to 9
move 1 from 2 to 8
move 1 from 1 to 9
move 7 from 9 to 1
move 1 from 8 to 5
move 7 from 1 to 7
move 3 from 5 to 8
move 3 from 7 to 2
move 1 from 8 to 4
move 1 from 2 to 4
move 2 from 4 to 6
move 5 from 3 to 1
move 9 from 7 to 2
move 6 from 3 to 8
move 8 from 2 to 7
move 2 from 6 to 4
move 2 from 1 to 7
move 2 from 1 to 4
move 24 from 7 to 4
move 4 from 8 to 9
move 2 from 7 to 5
move 1 from 5 to 2
move 1 from 3 to 8
move 4 from 2 to 8
move 13 from 9 to 2
move 2 from 8 to 6
move 3 from 9 to 6
move 26 from 4 to 2
move 1 from 5 to 7
move 2 from 6 to 2
move 2 from 4 to 1
move 7 from 2 to 1
move 15 from 2 to 6
move 8 from 2 to 8
move 4 from 6 to 8
move 9 from 2 to 9
move 13 from 6 to 7
move 6 from 1 to 9
move 2 from 2 to 4
move 4 from 1 to 6
move 3 from 8 to 3
move 1 from 4 to 9
move 2 from 6 to 7
move 1 from 4 to 3
move 3 from 3 to 2
move 14 from 7 to 4
move 5 from 9 to 5
move 9 from 8 to 5
move 7 from 9 to 6
move 2 from 5 to 6
move 2 from 9 to 2
move 10 from 5 to 1
move 1 from 3 to 1
move 2 from 8 to 1
move 1 from 9 to 2
move 1 from 7 to 5
move 4 from 2 to 1
move 1 from 9 to 8
move 3 from 4 to 1
move 1 from 8 to 6
move 12 from 1 to 5
move 1 from 1 to 6
move 1 from 7 to 5
move 4 from 6 to 9
move 2 from 2 to 4
move 1 from 9 to 6
move 1 from 1 to 5
move 2 from 9 to 7
move 10 from 6 to 5
move 1 from 6 to 7
move 20 from 5 to 1
move 1 from 7 to 9
move 2 from 9 to 1
move 3 from 5 to 1
move 2 from 8 to 4
move 2 from 8 to 7
move 1 from 5 to 9
move 1 from 8 to 4
move 22 from 1 to 7
move 5 from 4 to 8
move 1 from 5 to 9
move 19 from 7 to 4
move 2 from 9 to 1
move 1 from 5 to 9
move 10 from 1 to 8
move 1 from 9 to 1
move 1 from 8 to 3
move 8 from 4 to 7
move 1 from 5 to 6
move 3 from 4 to 5
move 1 from 5 to 9
move 11 from 7 to 4
move 4 from 4 to 9
move 1 from 6 to 2
move 1 from 3 to 9
move 5 from 9 to 4
move 5 from 7 to 9
move 23 from 4 to 2
move 17 from 2 to 7
move 2 from 2 to 8
move 4 from 4 to 7
move 1 from 4 to 5
move 2 from 5 to 2
move 5 from 8 to 9
move 5 from 2 to 7
move 9 from 7 to 5
move 11 from 9 to 2
move 1 from 4 to 3
move 5 from 8 to 7
move 3 from 8 to 5
move 2 from 1 to 3
move 2 from 3 to 9
move 1 from 5 to 8
move 5 from 7 to 5
move 15 from 5 to 4
move 2 from 8 to 1
move 2 from 5 to 1
move 4 from 4 to 1
move 1 from 8 to 7
move 8 from 2 to 1
move 4 from 2 to 8
move 2 from 7 to 4
move 5 from 8 to 6
move 5 from 7 to 9
move 4 from 6 to 5
move 7 from 4 to 8
move 1 from 6 to 1
move 1 from 3 to 1
move 2 from 5 to 1
move 7 from 1 to 5
move 5 from 1 to 3
move 4 from 7 to 9
move 4 from 3 to 9
move 2 from 9 to 7
move 6 from 9 to 2
move 1 from 4 to 1
move 1 from 3 to 5
move 1 from 2 to 5
move 5 from 9 to 4
move 4 from 4 to 6
move 1 from 8 to 9
move 8 from 4 to 3
move 7 from 7 to 3
move 5 from 1 to 3
move 11 from 5 to 9
move 1 from 7 to 6
move 2 from 3 to 5
move 1 from 3 to 1
move 3 from 6 to 2
move 2 from 5 to 1
move 2 from 1 to 2
move 3 from 1 to 5
move 5 from 9 to 2
move 2 from 6 to 8
move 2 from 3 to 8
move 4 from 9 to 7
move 3 from 5 to 2
move 2 from 1 to 8
move 1 from 9 to 8
move 1 from 9 to 2
move 4 from 7 to 9
move 11 from 8 to 7
move 1 from 8 to 2
move 6 from 9 to 7
move 3 from 7 to 1
move 13 from 2 to 7
move 24 from 7 to 1
move 2 from 2 to 6
move 1 from 8 to 3
move 1 from 9 to 3
move 5 from 2 to 4
move 1 from 2 to 5
move 1 from 6 to 2
move 1 from 6 to 3
move 1 from 2 to 4
move 3 from 7 to 3
move 2 from 1 to 7
move 2 from 3 to 8
move 2 from 7 to 8
move 9 from 3 to 2
move 3 from 4 to 8
move 1 from 5 to 1
move 9 from 2 to 1
move 3 from 4 to 9
move 1 from 7 to 8
move 6 from 3 to 9
move 2 from 1 to 5
move 15 from 1 to 3
move 13 from 3 to 9
move 11 from 1 to 4
move 5 from 4 to 1
move 6 from 3 to 6
move 4 from 4 to 8
move 6 from 1 to 4
move 1 from 5 to 2
move 1 from 2 to 1
move 3 from 4 to 2
move 2 from 8 to 5
move 2 from 4 to 2
move 9 from 9 to 3
move 9 from 3 to 5
move 2 from 9 to 4
move 5 from 2 to 6
move 1 from 1 to 8
move 1 from 4 to 1
move 10 from 9 to 2
move 9 from 2 to 4
move 10 from 4 to 1
move 3 from 1 to 3
move 4 from 1 to 2
move 5 from 2 to 4
move 2 from 5 to 2
move 4 from 1 to 7
move 10 from 5 to 4
move 2 from 2 to 4
move 1 from 9 to 2
move 2 from 3 to 5
move 1 from 3 to 5
move 3 from 6 to 7
move 8 from 4 to 9
move 6 from 6 to 1
move 4 from 9 to 5
move 2 from 9 to 1
move 1 from 2 to 6
move 6 from 5 to 2
move 3 from 7 to 9
move 4 from 8 to 2
move 1 from 7 to 9
move 1 from 5 to 3
move 2 from 7 to 4
move 1 from 7 to 1
move 14 from 1 to 9
move 1 from 1 to 9
move 1 from 3 to 8
move 3 from 2 to 5
move 2 from 4 to 2
move 6 from 8 to 1
move 1 from 2 to 1
move 5 from 1 to 9
move 1 from 1 to 7
move 2 from 8 to 5
move 1 from 5 to 4
move 1 from 6 to 1
move 8 from 2 to 7
move 2 from 6 to 1
move 9 from 9 to 5
move 11 from 4 to 8
move 4 from 7 to 4
move 6 from 4 to 6
move 1 from 7 to 4
move 6 from 6 to 7
move 1 from 5 to 9
move 6 from 8 to 9
move 8 from 9 to 5
move 1 from 4 to 5
move 15 from 9 to 3
move 3 from 1 to 4
move 6 from 7 to 2
move 3 from 4 to 9
move 2 from 7 to 3
move 1 from 7 to 3
move 1 from 7 to 2
move 2 from 8 to 1
move 3 from 8 to 5
move 2 from 1 to 7
move 8 from 3 to 6
move 3 from 6 to 5
move 1 from 6 to 1
move 10 from 5 to 7
move 6 from 5 to 4
move 4 from 2 to 4
move 6 from 5 to 1
move 6 from 1 to 8
move 2 from 9 to 2
move 2 from 9 to 7
move 6 from 3 to 7
move 1 from 3 to 5
move 1 from 1 to 9
move 2 from 8 to 1
move 2 from 5 to 4
move 3 from 3 to 7
move 10 from 4 to 6
move 1 from 9 to 7
move 12 from 7 to 3
move 12 from 3 to 8
move 2 from 1 to 5
move 1 from 1 to 3
move 13 from 8 to 1
move 7 from 7 to 1
move 13 from 6 to 9
move 1 from 7 to 4
move 6 from 5 to 3
move 3 from 4 to 3
move 6 from 3 to 1
move 10 from 9 to 4
move 2 from 7 to 6
move 8 from 1 to 9
move 3 from 2 to 9
move 1 from 3 to 5
move 1 from 3 to 5
move 1 from 1 to 4
move 6 from 9 to 3
move 2 from 6 to 7
move 4 from 9 to 5
move 4 from 1 to 6
move 1 from 2 to 4
move 6 from 1 to 4
move 3 from 9 to 3
move 3 from 6 to 8
move 3 from 8 to 7
move 5 from 5 to 1
move 1 from 3 to 9
move 1 from 9 to 5
move 1 from 3 to 2
move 2 from 5 to 1
move 1 from 6 to 9
move 1 from 6 to 3
move 2 from 9 to 7
move 2 from 8 to 1
move 1 from 3 to 2
move 1 from 2 to 5
move 1 from 7 to 1
move 7 from 7 to 9
move 12 from 1 to 9
move 1 from 5 to 2
move 1 from 7 to 1
move 13 from 4 to 7
move 1 from 9 to 4
move 5 from 7 to 3
move 4 from 9 to 1
move 8 from 7 to 9
move 3 from 2 to 3
move 4 from 3 to 7
move 5 from 4 to 6
move 3 from 9 to 4
move 10 from 1 to 5
move 3 from 4 to 7
move 16 from 9 to 2
move 3 from 9 to 2
move 6 from 5 to 3
move 4 from 6 to 2
move 1 from 4 to 6
move 2 from 6 to 8
move 1 from 5 to 2
move 1 from 5 to 8
move 7 from 7 to 2
move 16 from 2 to 1
move 1 from 5 to 1
move 10 from 2 to 8
move 14 from 8 to 5
move 2 from 2 to 6
move 1 from 2 to 5
move 2 from 2 to 1
move 8 from 1 to 7
move 4 from 1 to 7
move 2 from 1 to 7
move 5 from 3 to 2
move 1 from 1 to 6
move 2 from 2 to 5
move 4 from 1 to 7
move 1 from 2 to 8
move 1 from 2 to 8
move 3 from 6 to 7
move 10 from 7 to 5
move 1 from 2 to 8
move 27 from 5 to 9
move 1 from 5 to 6
move 1 from 6 to 4
move 1 from 4 to 3
move 3 from 3 to 7
move 4 from 3 to 6
move 2 from 6 to 4
move 3 from 8 to 1
move 2 from 6 to 1
move 12 from 7 to 8
move 2 from 3 to 9
move 1 from 9 to 2
move 1 from 2 to 8
move 2 from 1 to 2
move 6 from 3 to 8
move 1 from 7 to 4
move 15 from 9 to 5
move 7 from 9 to 4
move 1 from 2 to 1
move 16 from 8 to 2
move 8 from 5 to 2
move 24 from 2 to 9
move 3 from 1 to 2
move 24 from 9 to 1
move 5 from 5 to 9
move 3 from 4 to 1
move 1 from 7 to 6
move 1 from 6 to 3
move 1 from 3 to 2
move 3 from 2 to 3
move 1 from 5 to 6
move 1 from 2 to 7"""

sample_directions = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

crates = [
    ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    ['T', 'B', 'M', 'Z', 'R'],
    ['Z', 'L', 'C', 'H', 'N', 'S'],
    ['S', 'C', 'F', 'J'],
    ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    ['M', 'Z', 'R'],
    ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
]

sample_crates = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P'],
]


# Parse directions as:
# Move #, from #, to #
def parse(input: str):
    def parse_direction(x):
        x = re.split(' from | to ', x.replace('move ', ''))
        return list(map(int, x))

    return list(map(parse_direction, input.split('\n')))


# Array slicing
# Move will reverse order of array


def apply_directions(directions_list: list, crates_list: list):
    for d in directions_list:
        move_crates(d[0], d[1], d[2], crates_list)
    # move_crates(directions_list[0][0], directions_list[0][1], directions_list[0][2], crates_list)
    # print(crates_list)
    # move_crates(directions_list[1][0], directions_list[1][1], directions_list[1][2], crates_list)


def move_crates(amount: int, move_from: int, move_to: int, crate_stacks: list):
    while amount > 0:
        lift = crate_stacks[move_from - 1].pop(-1)
        crate_stacks[move_to - 1].append(lift)
        amount -= 1


def gather_top_crates(crate_stacks: list):
    tops = []
    for c in crate_stacks:
        tops.append(c.pop())

    return ''.join(tops)


# Part 1 - Sample
print(sample_crates)
# Note: In place
apply_directions(parse(sample_directions), sample_crates)
print(sample_crates)
print(gather_top_crates(sample_crates))

# Part 1 - Actual
print(crates)
# Note: In place
apply_directions(parse(directions), crates)
print(crates)
print(gather_top_crates(crates))
