from src import main


def test_hello():
    assert main.hello() == 'hello'

def test_goodbye():
    assert main.goodbye() == 'goodbye'


