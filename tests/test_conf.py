import pytest

l = [50, 60, 100]


def test_01(tmp_file):
    file_name = tmp_file()
    with open(file_name, 'w') as f:
        f.write(str(range(100)))

    assert isinstance(file_name, str)


@pytest.mark.parametrize("i", l)
def test_param(i):
    assert i >= 50
