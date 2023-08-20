import tempfile

import pytest


@pytest.fixture(scope="function")
def tmp_file():
    def create() -> str:
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name

    return create
