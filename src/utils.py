import os


def read_file(day: int, transform, use_test = False) -> list:
    try:
        if use_test:
            with open(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'Input_Files', f'day_{day}_test.txt')) as f:
                return [transform(line.strip()) for line in f]
        else:
            with open(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'Input_Files', f'day_{day}.txt')) as f:
                return [transform(line.strip()) for line in f]
    except FileNotFoundError as e:
        print(e)
