import pytest

test_list = [str(i) for i in range(10)] + ['not digit', 'string']


@pytest.mark.parametrize("item", test_list)
def test_string_is_digit(item) -> None:
    assert item.isdigit()
