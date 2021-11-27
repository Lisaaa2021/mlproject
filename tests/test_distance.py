from mlproject.distance import haversine


def test_haversine():
    assert isinstance(haversine(1,2,3,4), float)
