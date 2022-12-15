sample_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

baby_data = """noop
addx 3
addx -5"""


data = """addx 1
noop
addx 4
noop
noop
noop
addx 6
addx -1
addx 5
noop
noop
noop
addx 5
addx -14
noop
addx 19
noop
addx 1
addx 4
addx 1
noop
noop
addx 2
addx 5
addx -27
addx 20
addx -30
addx 2
addx 5
addx 2
addx 4
addx -3
addx 2
addx 5
addx 2
addx -9
addx 1
addx 11
noop
addx -20
addx 7
addx 23
addx 2
addx 3
addx -2
addx -34
addx -2
noop
addx 3
noop
addx 3
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx -9
addx -7
addx 21
noop
addx 8
noop
addx -1
addx 3
addx -2
addx 5
addx -37
noop
addx 35
addx -31
addx 1
addx 4
addx -1
addx 2
noop
addx 3
addx 1
addx 5
addx -2
addx 7
addx -2
addx -2
addx 10
noop
addx 4
noop
noop
addx -19
addx 20
addx -38
noop
noop
addx 7
addx 2
addx 3
noop
addx 4
addx -3
addx 2
addx 2
noop
addx 3
noop
noop
noop
addx 5
noop
addx 7
addx -2
addx 7
noop
noop
addx -5
addx 6
addx -36
noop
addx 1
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 5
addx 2
addx 1
noop
addx 4
addx -16
addx 21
noop
noop
addx 1
addx -8
addx 12
noop
noop
noop
noop"""


def parse(i: str):
    def split_str(x):
        return x.split(' ')
    return list(map(split_str, i.split('\n')))


commands = parse(data)

register = 1
cycles = [1]
cycle = 0

while len(commands) > 0:
    cmd = commands.pop(0)
    cycle += 1
    # print('start cycle: ', cycle, 'reg: ', register)
    cycles.append(register)

    # if cmd[0] == 'noop':
    if cmd[0] == 'addx':
        cycle += 1
        # print('start cycle: ', cycle, 'reg: ', register)
        cycles.append(register)

        register = register + int(cmd[1])

    # print('cmd: ', cmd)
    # print('register: ', register)
    # print('cycle: ', cycle, 'cycles len: ', len(cycles))
    # print('cycles: ', cycles)


# print(cycles[20])
# print(cycles[60])
# print(cycles[100])
# print(cycles[140])
# print(cycles[180])
# print(cycles[220])

a = sum([
    cycles[20] * 20,
    cycles[60] * 60,
    cycles[100] * 100,
    cycles[140] * 140,
    cycles[180] * 180,
    cycles[220] * 220]
)

# print(a)


def draw(start, end):
    s = ''
    for x in range(start, end):
        val = cycles[x]
        # print('x: ', x, 'x%40', x%40, 'val: ', val, 'Result:', val - 1 <= x - 1 <= val + 1)
        x = x % 40

        if val - 1 <= x - 1 <= val + 1:
            s += '#'
        else:
            s += '.'

    print(s)


draw(1, 41)
draw(41, 81)
draw(81, 121)
draw(121, 161)
draw(161, 201)
draw(201, 241)

# ####.###...##..###..#....####.####.#..#.
# ...#.#..#.#..#.#..#.#....#.......#.#..#.
# ..#..#..#.#..#.#..#.#....###....#..#..#.
# .#...###..####.###..#....#.....#...#..#.
# #....#.#..#..#.#.#..#....#....#....#..#.
# ####.#..#.#..#.#..#.####.#....####..##..

# Part 2 Answer: ZRARLFZU