import sys
from collections import deque
from math import lcm

from utils import read_file

values = read_file(11, str, False)


class Monkey:
    monkey_id: int
    items: deque
    operation: list
    test_number: int
    true_id: int
    false_id: int
    total_inspections: int

    def __init__(self, monkey_id, items, operation, test_number, true_id, false_id):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.true_id = true_id
        self.false_id = false_id
        self.total_inspections = 0

    def run_operation(self, item, divider ,relief = True):
        self.total_inspections += 1
        if self.operation[0] == '*':
            if self.operation[1] == 'old':
                item *= item
            else:
                item *= int(self.operation[1])
        if self.operation[0] == '+':
            if self.operation[1] == 'old':
                item += item
            else:
                item += int(self.operation[1])

        item = item % divider
        if relief:
            return int(item / 3)
        return item

    def run_test(self, item):
        if item % self.test_number == 0:
            return self.true_id
        return self.false_id

    def __repr__(self):
        return f'Monkey: {self.monkey_id}, Items: {self.items}'


values = [value for value in values if value != '']

# Part 1
monkeys = []
_id = 0
for i in range(0, len(values), 6):
    _starting_items = values[i + 1].split()[2:]
    _starting_items = [int(n.strip(',')) for n in _starting_items]
    _items = deque(_starting_items)
    _operation = values[i + 2].split()[4:]
    _test_number = int(values[i + 3].split()[3])
    _true_id = int(values[i + 4].split()[5])
    _false_id = int(values[i + 5].split()[5])
    monkey = Monkey(_id, _items, _operation, _test_number, _true_id, _false_id)
    _id += 1
    monkeys.append(monkey)

rounds = 1
while rounds < 21:
    for monkey in range(len(monkeys)):
        for i in range(len(monkeys[monkey].items)):
            current_item = monkeys[monkey].items.popleft()
            _divider = lcm(*[monkey.test_number for monkey in monkeys])
            inspection = monkeys[monkey].run_operation(current_item, _divider)
            throw_id = monkeys[monkey].run_test(inspection)
            monkeys[throw_id].items.append(inspection)
    rounds += 1
    sys.stdout.write("\rRounds completed %i" % rounds)
    sys.stdout.flush()

all_inspections = []
for monkey in range(len(monkeys)):
    all_inspections.append(monkeys[monkey].total_inspections)

all_inspections = sorted(all_inspections, reverse=True)
print()
print(f'Part 1: {all_inspections[0] * all_inspections[1]}')
# Part 1: 58056

# Part 2

monkeys = []
_id = 0
for i in range(0, len(values), 6):
    _starting_items = values[i + 1].split()[2:]
    _starting_items = [int(n.strip(',')) for n in _starting_items]
    _items = deque(_starting_items)
    _operation = values[i + 2].split()[4:]
    _test_number = int(values[i + 3].split()[3])
    _true_id = int(values[i + 4].split()[5])
    _false_id = int(values[i + 5].split()[5])
    monkey = Monkey(_id, _items, _operation, _test_number, _true_id, _false_id)
    _id += 1
    monkeys.append(monkey)

rounds = 1
while rounds < 10001:
    for monkey in range(len(monkeys)):
        for i in range(len(monkeys[monkey].items)):
            current_item = monkeys[monkey].items.popleft()
            _divider = lcm(*[monkey.test_number for monkey in monkeys])
            inspection = monkeys[monkey].run_operation(current_item, _divider, False)
            throw_id = monkeys[monkey].run_test(inspection)
            monkeys[throw_id].items.append(inspection)
    rounds += 1
    sys.stdout.write("\rRounds completed %i" % rounds)
    sys.stdout.flush()

all_inspections = []
for monkey in range(len(monkeys)):
    all_inspections.append(monkeys[monkey].total_inspections)

all_inspections = sorted(all_inspections, reverse=True)
print(f'Part 2: {all_inspections[0] * all_inspections[1]}')
# Part 2: 15048718170