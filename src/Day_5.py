from utils import read_file

values = read_file(5, str, True, False)

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
# print(total_columns)

stacks = []
# print(stack_strings)
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
    stacks.append(row)

print(stacks)

print(instruction_strings)
instructions = []
for s in instruction_strings:
    instruction = []
    split = s.split(' ')
    instruction.append(int(split[1]))
    instruction.append(int(split[3]) - 1)
    instruction.append(int(split[5]) - 1)
    instructions.append(instruction)


# for instruction in instructions:
#     amount = instruction[0]
#     start = instruction[1]
#     end = instruction[2]
#     for i in range(amount):
#         crate = stacks[0][start]
#         stacks[0][start] = ''
#         stacks[0][end] = crate

instruction = instructions[0]
amount = instruction[0]
start = instruction[1]
end = instruction[2]
for i in range(amount):
    crate = stacks[0][start]
    stacks[0][start] = ''
    stacks[0][end] = crate

print(stacks)

instruction = instructions[1]
amount = instruction[0]
start = instruction[1]
end = instruction[2]
for i in range(amount):
    crate = stacks[0][start]
    stacks[0][start] = ''

    stacks[0][end] = crate

print(stacks)

