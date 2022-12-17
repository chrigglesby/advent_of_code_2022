import operator

sample_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


# Loop input
# Create monkeys (Class) from input

# For each monkey
# Inspect each item
# Set the new worry value
# Divide by 3 for relief, round down to int

# On monkey turn
# Inspect each
# Throw each (based on decision)

# Count the total number of inspections a monkey does (over 20 rounds)
# Monkey business = top two inspection counts multiplied
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class Operation:
    def __init__(self, operand, value):
        self.operand = operand
        self.value = value

    def do_op(self, target: int):
        global ops
        value = self.value
        if self.value == 'old':
            value = target

        return ops[self.operand](int(target), int(value))


class Ape:
    number: int
    items: list
    operation: Operation


def parse(input: str):
    input = input.split('\n')

    tribe = []
    current_ape = Ape()

    for line in input:
        if 'Monkey ' in line:
            # New Ape
            current_ape.number = int(line[7:-1])
        elif '  Starting items: ' in line:
            current_ape.items = list(map(int, line[18:].split(', ')))
        elif '  Operation: new = ' in line:
            tov = line[19:].split(' ')
            current_ape.operation = Operation(
                operand=tov[1],
                value=tov[2]
            )

            # Last step is
            # Add ape to tribe
            tribe.append(current_ape)
            # Reset current_ape
            current_ape = Ape()

    return tribe


def relief(x: int):
    return x // 3


apes = parse(sample_data)

for ape in apes:
    print('Monkey: ', ape.number)
    print(' Operation: ', ape.operation.operand, ape.operation.value)
    for idx, item in enumerate(ape.items):
        print('  Inspecting: ', item)
        worry_applied_item = ape.operation.do_op(item)
        # Overwrite item with new worry value
        ape.items[idx] = worry_applied_item
        print('  Worry multiplier applied: ', worry_applied_item)
        relief_applied_item = relief(worry_applied_item)
        print('  Relief multiplier applied: ', relief_applied_item)
        # Overwrite item with new worry value
        ape.items[idx] = relief_applied_item



