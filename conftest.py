import pytest


@pytest.fixture()
def browser():
    print("\nStart test")
    yield
    print("\nFinish test")