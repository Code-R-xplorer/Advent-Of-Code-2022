from utils import read_file

values = read_file(7, str, False)


class Node:
    def __init__(self, name, size, is_dir):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def calculate_size(self):
        size = self.size
        for child in self.children:
            size += child.calculate_size()
        return size

    def sum_size(self, threshold):
        if not self.is_dir:
            return 0
        elif self.calculate_size() <= threshold:
            return self.calculate_size() + sum(child.sum_size(threshold) for child in self.children)
        else:
            return sum(child.sum_size(threshold) for child in self.children)

    def get_larger_than(self, threshold):
        if not self.is_dir:
            return None
        elif self.calculate_size() >= threshold:
            return [self.calculate_size()] + [child.get_larger_than(threshold) for child in self.children if
                                              child.get_larger_than(threshold)]
        else:
            return None


# Build File System
root = Node('/', 0, True)
current = root
for value in values:
    line = value.split()
    # Line is a command
    if line[0] == '$':
        # Command is a change directory command
        if line[1] == 'cd':
            # Blank cd command goes back to root
            if len(line) == 2:
                current = root
            # .. goes back one directory
            elif line[2] == '..':
                current = current.parent
            # Moving into a directory
            else:
                # Move to root directory
                if line[2] == '/':
                    current = root
                # Move to specified directory
                else:
                    parent = current
                    current = [_dir for _dir in current.children if _dir.name == line[2]][0]
                    current.set_parent(parent)
    # Line is a directory
    elif line[0] == 'dir':
        node = Node(line[1], 0, True)
        current.add_child(node)
    # Line is a file
    else:
        node = Node(line[1], int(line[0]), False)
        current.add_child(node)

# print("Part 1: " + str(root.sum_size(100000)))
# Part 1: 1423358

total_disk_size = 70000000
update_size = 30000000

needed_space = update_size - (total_disk_size - root.calculate_size())


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


directory_candidates = flatten(root.get_larger_than(needed_space))
print(min(directory_candidates))
