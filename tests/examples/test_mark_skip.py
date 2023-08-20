import pytest


@pytest.mark.skip
def test_skip() -> None:
    assert False


@pytest.mark.skipif(True, reason="Testing Skip")
def test_skipif() -> None:
    assert False


def test_noskip() -> None:
    assert False
