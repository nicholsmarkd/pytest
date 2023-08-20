import pytest


@pytest.mark.xfail
def test_fail() -> None:
    assert False
