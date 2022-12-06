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

# print(stacks)

# print(instruction_strings)
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
        if stacks[0][start] != '':
            crate = stacks[0][start]
            stacks[0][start] = ''
        else:
            for x in range(len(stacks)):
                if stacks[x][start] != '':
                    crate = stacks[x][start]
                    stacks[x][start] = ''
                    break
        for x in reversed(range(len(stacks))):
            if stacks[x][end] == '':
                stacks[x][end] = crate
                crate = ''
                break
        if crate != '':
            new_row = []
            for _ in range(total_columns):
                new_row.append('')
            stacks.insert(0, new_row)
            stacks[0][end] = crate

top_crates = []

for _ in range(total_columns):
    top_crates.append('')


for row in reversed(range(len(stacks))):
    for column in range(len(stacks[row])):
        if stacks[row][column] != '':
            top_crates[column] = stacks[row][column]

message = ''

for crate in top_crates:
    message += crate
print("Part 1: " + message)

# Part 1 = SHMSDGZVC

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

for instruction in instructions:
    # print(stacks)
    amount = instruction[0]
    start = instruction[1]
    end = instruction[2]
    start_index = amount
    end_index = len(stacks) - amount
    for i in reversed(range(amount)):
        if stacks[i][start] != '':
            crate = stacks[i][start]
            stacks[i][start] = ''
        elif amount == 1:
            for j in reversed(range(len(stacks))):
                if stacks[j][start] == '':
                    crate = stacks[j + 1][start]
                    stacks[j + 1][start] = ''
                    break
        else:
            for x in reversed(range(len(stacks))):
                if stacks[x][start] != '':
                    crate = stacks[x][start]
                    stacks[x][start] = ''
                    break
            # for x in range(len(stacks)):
            #     if stacks[x][start] != '':
            #         crate = stacks[x][start]
            #         stacks[x][start] = ''
            #         break
        for x in reversed(range(len(stacks))):
            if stacks[x][end] == '':
                stacks[x][end] = crate
                crate = ''
                break
        if crate != '':
            new_row = []
            for _ in range(total_columns):
                new_row.append('')
            stacks.insert(0, new_row)
            stacks[0][end] = crate

    print("--------------After Instruction-------------------")
    for stack in stacks:
        print(stack)

print("--------------Final-----------------")
for stack in stacks:
    print(stack)

top_crates = []

for _ in range(total_columns):
    top_crates.append('')


for row in reversed(range(len(stacks))):
    for column in range(len(stacks[row])):
        if stacks[row][column] != '':
            top_crates[column] = stacks[row][column]

message = ''

for crate in top_crates:
    message += crate
print("Part 2: " + message)



# instruction = instructions[0]
# amount = instruction[0]
# start = instruction[1]
# end = instruction[2]
# for i in range(amount):
#     crate = stacks[0][start]
#     stacks[0][start] = ''
#     stacks[0][end] = crate
#
# print(stacks)
#
# instruction = instructions[1]
# amount = instruction[0]
# start = instruction[1]
# end = instruction[2]
# for i in range(amount):
#     if stacks[0][start] != '':
#         crate = stacks[0][start]
#         stacks[0][start] = ''
#     else:
#         for x in range(len(stacks)):
#             if stacks[x][start] != '':
#                 crate = stacks[x][start]
#                 stacks[x][start] = ''
#                 break
#     for x in reversed(range(len(stacks))):
#         if stacks[x][end] == '':
#             stacks[x][end] = crate
#             crate = ''
#             break
#     if crate != '':
#         new_row = []
#         for _ in range(total_columns):
#             new_row.append('')
#         stacks.insert(0, new_row)
#         stacks[0][end] = crate
#
# print(stacks)

#
# for row in reversed(range(len(stacks))):
#     clear_row = True
#     for column in reversed(range(len(stacks[row]))):
#         if stacks[row][column] != '':
#             clear_row = False
#             break
#     if clear_row:
#         stacks.pop(row)
#
# print(stacks)


