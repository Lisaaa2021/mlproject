from mlproject.lib import hello_world


def test_length_of_hello_world():
    assert len(hello_world()) != 0


def test_try_me():
    assert 'matrix' in try_me()
