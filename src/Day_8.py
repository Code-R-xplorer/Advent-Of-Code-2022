from utils import read_file

values = read_file(8, str, False)

grid = []

for current_tree_height in values:
    grid.append(list(current_tree_height))

visible = 0


def get_column(matrix, i):
    return [_row[i] for _row in matrix]


for row in range(len(grid)):
    for column in range(len(grid[row])):
        # Ignore Edges
        if row == 0 or row == len(grid) - 1 or column == 0 or column == len(grid[row]) - 1:
            visible += 1
            continue
        # Current tree height to compare to
        current_tree_height = grid[row][column]
        current_column = get_column(grid, column)
        current_row = grid[row]
        up = current_column[0:row]
        down = current_column[row + 1:]
        left = current_row[0:column]
        right = current_row[column + 1:]
        from_left = len([tree for tree in left if tree >= current_tree_height]) == 0
        from_right = len([tree for tree in right if tree >= current_tree_height]) == 0
        from_up = len([tree for tree in up if tree >= current_tree_height]) == 0
        from_down = len([tree for tree in down if tree >= current_tree_height]) == 0
        if from_up or from_down or from_left or from_right:
            visible += 1

print("Part 1: " + str(visible))
# Part 1: 1809
