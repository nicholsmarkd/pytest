import os


def get_stuff() -> str:
    cwd: str = os.getcwd()
    print(cwd)
    return cwd
