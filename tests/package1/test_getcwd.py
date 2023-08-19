from src.package1 import get_stuff


def test_get_cwd() -> None:
    cwd = get_stuff()
    print(cwd)

    assert cwd is not None
