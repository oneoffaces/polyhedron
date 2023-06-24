from common.r3 import R3


class TestR3:

    def test_distance(self):
        a = R3(0.0, 0.0, 0.0)
        b = R3(1.0, 2.0, 2.0)
        assert a.distance(b) == 3.0

    def test_is_good1(self):
        a = R3(0.1, 0.2, 0.3)
        assert a.is_good()

    def test_is_good2(self):
        a = R3(1.0, 2.0, 3.0)
        assert not(a.is_good())
