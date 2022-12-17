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


class Test:
    def __init__(self, test, true_case: int, false_case: int):
        self.test = test
        self.true_case = true_case  # Monkey # to throw to
        self.false_case = false_case  # Monkey # to throw to

    def get_outcome(self, value):
        if 'divisible by ' in self.test:
            by = int(self.test[13:])
            return self.true_case if value % by == 0 else self.false_case
        else:
            raise ValueError('Test is NOT divisible by')


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
    test: Test
    inspect_count = 0

    def apply_worry_relief(self):
        for idx, item in enumerate(self.items):
            print('  Inspecting: ', item)
            worry_applied_item = self.operation.do_op(item)
            print('  Worry multiplier applied: ', worry_applied_item)
            relief_applied_item = relief(worry_applied_item)
            print('  Relief multiplier applied: ', relief_applied_item)
            # Overwrite item with new worry value
            self.items[idx] = relief_applied_item
            # Increment inspect_count
            self.inspect_count += 1

    def do_throws(self):
        for i in range(len(self.items)):
            to_throw = self.items.pop(0)  # Current item
            print('    Deciding where to throw: ', to_throw)
            # Monkey makes decision
            monkey_to_throw_to = self.test.get_outcome(to_throw)

            print('      Throwing to: ', monkey_to_throw_to)
            # Monkey throws
            apes[monkey_to_throw_to].items.append(to_throw)


def parse(input: str):
    input = input.split('\n')

    tribe = []
    current_ape = Ape()

    for i, line in enumerate(input):
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

        elif '  Test: ' in line:
            # On 'Test:' line, grab next two lines for processing
            t = line[8:]  # This is always 'Test: divisible by '
            tc = int(input[i + 1][29:])
            fc = int(input[i + 2][30:])

            current_ape.test = Test(
                test=t,
                true_case=tc,
                false_case=fc
            )

            # Last step is
            # Add ape to tribe
            tribe.append(current_ape)
            # Reset current_ape
            current_ape = Ape()

    return tribe


def relief(x: int):
    return x // 3


def do_round():
    global apes
    # This is a Round
    # All Apes, All Items, Inspection Worry and Relief Applied, Items Thrown
    for ape in apes:
        print('Monkey: ', ape.number)
        print(' Operation: ', ape.operation.operand, ape.operation.value)
        ape.apply_worry_relief()
        ape.do_throws()


apes = parse(sample_data)


for i in range(20):
    do_round()


inspect_counts = []
for a in apes:
    inspect_counts.append(a.inspect_count)

inspect_counts = sorted(inspect_counts)
monkey_business = inspect_counts[-1] * inspect_counts[-2]
print(monkey_business)

