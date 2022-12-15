from utils import read_file

values = read_file(10, str, False)

instructions = []

for value in values:
    instructions.append(value.split())

# Part 1

# cycles = 1
# X = 1
# instruction_id = 0
#
# cycle_count = 1
# cycle_check = 20
#
# signal_strength = 0
#
# while cycles < 220:
#     cycles += 1
#     current_instruction = instructions[instruction_id]
#     if current_instruction[0] == 'addx':
#         if cycles == cycle_count + 2:
#             X += int(current_instruction[1])
#             instruction_id += 1
#             cycle_count = cycles
#     if current_instruction[0] == 'noop':
#         instruction_id += 1
#         cycle_count = cycles
#
#     if cycles == cycle_check:
#         signal_strength += cycle_check * X
#         cycle_check += 40
#
# print(f'Part 1: {signal_strength}')
# Part 1: 15020


# Part 2

cycles = 0
cycle_count = 1
X = 1
instruction_id = 0

image = []
sprite_position = 1
current_row = []
draw_pos = -1
while cycles < 240:
    cycles += 1
    current_instruction = instructions[instruction_id]
    if current_instruction[0] == 'addx':
        if cycles == cycle_count + 2:
            X += int(current_instruction[1])
            sprite_position += int(current_instruction[1])
            instruction_id += 1
            cycle_count = cycles
    if current_instruction[0] == 'noop':
        instruction_id += 1
        cycle_count = cycles

    draw_pos += 1
    if draw_pos in [sprite_position - 1, sprite_position, sprite_position + 1]:
        current_row.append('#')
    else:
        current_row.append('.')

    if cycles % 40 == 0:
        image.append(current_row)
        current_row = []
        draw_pos = -1

for x in range(len(image)):
    for y in range(len(image[x])):
        print(image[x][y], end="")
    print()

# Part 2: EFUGLPAP
# ####.####.#..#..##..#....###...##..###..
# #....#....#..#.#..#.#....#..#.#..#.#..#.
# ###..###..#..#.#....#....#..#.#..#.#..#.
# #....#....#..#.#.##.#....###..####.###..
# #....#....#..#.#..#.#....#....#..#.#....
# ####.#.....##...###.####.#....#..#.#....
