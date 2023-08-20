import os
from src.main import is_done


class TestIsDone:

    def setup_method(self):
        self.test_file = "/tmp/test_file"

    def teardown_method(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def write_tmp_file(self, content):
        with open(self.test_file, "w") as _f:
            _f.write(content)

    def test_yes(self):
        self.write_tmp_file("yes")
        assert is_done(self.test_file) is True

    def test_no(self):
        self.write_tmp_file("no")
        assert is_done(self.test_file) is False
