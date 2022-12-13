from utils import read_file

values = read_file(7, str, True)


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

    def __repr__(self):
        if self.is_dir:
            return f'{f"/{self.name}"}" children={self.children} size={self.calculate_size()}>'
        else:
            return f'{self.name}" size={self.size}>'


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
        node = Node(line[1], int(line[0]), True)
        current.add_child(node)

