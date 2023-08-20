import pytest


def test_raises_pass() -> None:
    with pytest.raises(TypeError):
        assert 1 + "a", "Should PASS as it raises a TypeError"


@pytest.mark.xfail
def test_raises_fail() -> None:
    with pytest.raises(TypeError):
        assert 1 + 1, "Should FAIL as it does not raise a TypeError"
