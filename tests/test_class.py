from src.main import hello


class TestAll:

    def test_hello(self):
        assert hello() == 'hello'
