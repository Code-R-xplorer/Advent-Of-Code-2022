from utils import read_file

values = read_file(10, str, False)

instructions = []

for value in values:
    instructions.append(value.split())

cycles = 1
X = 1
instruction_id = 0

cycle_count = 1
cycle_check = 20

signal_strength = 0

while cycles < 220:
    cycles += 1
    current_instruction = instructions[instruction_id]
    if current_instruction[0] == 'addx':
        if cycles == cycle_count + 2:
            X += int(current_instruction[1])
            instruction_id += 1
            cycle_count = cycles
    if current_instruction[0] == 'noop':
        instruction_id += 1
        cycle_count = cycles

    if cycles == cycle_check:
        signal_strength += cycle_check * X
        cycle_check += 40

print(f'Part 1: {signal_strength}')
