import os


def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)
