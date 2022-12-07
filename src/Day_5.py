from collections import deque

from utils import read_file

values = read_file(5, str, False, False)

stack_strings = []
instruction_strings = []


end_stack = False
for value in values:
    if end_stack:
        instruction_strings.append(value)
    elif value == '':
        end_stack = True
    else:
        stack_strings.append(value)

total_columns = stack_strings.pop()
tmp = total_columns.split(' ')
total_columns = int(tmp[len(tmp) - 1])

stacks_strings = []
for stack_string in stack_strings:
    row = []
    split_stack_string = stack_string.split(' ')
    column_counter = 0
    for s in split_stack_string:
        if s == '':
            column_counter += 1
        if column_counter == 4:
            row.append('')
            column_counter = 0
        if '[' in s:
            row.append(s.strip('[]'))
    if len(row) < total_columns:
        for i in range(total_columns - len(row)):
            row.append('')
    stacks_strings.append(row)

stacks = []

for y in range(len(stacks_strings[len(stacks_strings) - 1])):
    stacks.append(deque(stacks_strings[len(stacks_strings) - 1][y]))

for row in reversed(range(len(stacks_strings)-1)):
    for column in range(len(stacks_strings[row])):
        if stacks_strings[row][column] != '':
            stacks[column].append(stacks_strings[row][column])

instructions = []
for s in instruction_strings:
    instruction = []
    split = s.split(' ')
    instruction.append(int(split[1]))
    instruction.append(int(split[3]) - 1)
    instruction.append(int(split[5]) - 1)
    instructions.append(instruction)

for instruction in instructions:
    amount = instruction[0]
    start = instruction[1]
    end = instruction[2]
    for i in range(amount):
        crate = stacks[start].pop()
        stacks[end].append(crate)

message = ''

for stack in stacks:
    crate = stack.pop()
    message += crate

print("Part 1: " + message)
# Part 1: SHMSDGZVC

stacks = []

for y in range(len(stacks_strings[len(stacks_strings) - 1])):
    stacks.append(deque(stacks_strings[len(stacks_strings) - 1][y]))

for row in reversed(range(len(stacks_strings)-1)):
    for column in range(len(stacks_strings[row])):
        if stacks_strings[row][column] != '':
            stacks[column].append(stacks_strings[row][column])


for instruction in instructions:
    amount = instruction[0]
    start = instruction[1]
    end = instruction[2]
    tmp_stack = list()
    for i in range(amount):
        tmp_stack.append(stacks[start].pop())
    for i in range(amount):
        stacks[end].append(tmp_stack.pop())


message = ''

for stack in stacks:
    crate = stack.pop()
    message += crate

print("Part 2: " + message)
# Part 2: VRZGHDFBQ
