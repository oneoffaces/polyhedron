from shadow.polyedr import Polyedr


class TestPolyedr:

    def test_polyedr_1(self):
        assert Polyedr(f"data/test1.geom").length() == 12

    def test_polyedr_2(self):
        assert Polyedr(f"data/test2.geom").length() == 16

    def test_polyedr_3(self):
        assert Polyedr(f"data/test3.geom").length() == 16

    def test_polyedr_4(self):
        assert Polyedr(f"data/test4.geom").length() == 24

    def test_polyedr_5(self):
        assert Polyedr(f"data/test5.geom").length() == 20

    def test_polyedr_6(self):
        assert Polyedr(f"data/test6.geom").length() == 24

    def test_polyedr_7(self):
        assert Polyedr(f"data/test7.geom").length() == 20
