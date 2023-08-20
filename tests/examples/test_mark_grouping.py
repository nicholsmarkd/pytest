import pytest


@pytest.mark.grp01
def test_first_group_a() -> None:
    assert True, "This is a test in group 1"


@pytest.mark.grp01
def test_first_group_b() -> None:
    assert True, "This is a test in group 1"


@pytest.mark.grp02
def test_second_group_a() -> None:
    assert True, "This is a test in group 2"


