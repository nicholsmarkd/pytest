import pytest


@pytest.mark.parametrize("i", [40,50,60])
def test_parametrize(i) -> None:
    assert i >= 50