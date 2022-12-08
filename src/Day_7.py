from utils import read_file
from dataclasses import dataclass, field

values = read_file(7, str, True)


@dataclass
class Directory:
    name: str = ""
    contents: list = field(default_factory=list)


@dataclass
class File:
    name: str
    size: int


root = Directory()


for value in values:
    line = value.split()
    # User Command
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                root.name = '/'


print(root)
