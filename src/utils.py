import os


def read_file(day: int, transform=str, use_test = False, strip_line = True) -> list:
    try:
        if use_test:
            with open(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'Input_Files', f'day_{day}_test.txt')) as f:
                if strip_line:
                    return [transform(line.strip()) for line in f]
                else:
                    return [transform(line.strip('\n')) for line in f]
        else:
            with open(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'Input_Files', f'day_{day}.txt')) as f:
                if strip_line:
                    return [transform(line.strip()) for line in f]
                else:
                    return [transform(line.strip('\n')) for line in f]
    except FileNotFoundError as e:
        print(e)
