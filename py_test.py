import pytest

from animal import Point2D, Point3D


class TestPoint2D:

    # @pytest.mark.parametrize("test_string, expected", [(str(test_string),
    # 'Point 2, 5')])
    def test_string_method_class(self):
        point = Point2D(2, 5)
        assert point.__str__() == 'Point 2, 5'

    def test_calculate_distance_beetwen_two_points(self):
        point = Point2D(1, 5)
        distance = point.calculate_distance_beetwen_two_points(8, 9)
        assert distance == 8.062

class TestPoint3D:

    def test_string_method_class(self):
        point = Point3D(2, 5, 8)
        assert point.__str__() == 'Point 2, 5, 8'
