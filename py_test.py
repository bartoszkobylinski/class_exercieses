import pytest

from animal import Point2D, Point3D, Worker


class TestPoint2D:

    @pytest.mark.parametrize("point_name, expected", [("point_name",
                                                       "Point 2, 5")])
    def test_string_method_class(self, point_name, expected):
        point = Point2D(2, 5)
        point_name = point.__str__()
        assert point_name == expected

    @pytest.mark.parametrize("distance, expected", [("distance", 8.062)])
    def test_calculate_distance_beetwen_two_points(self, distance, expected):
        point = Point2D(1, 5)
        distance = point.calculate_distance_beetwen_two_points(8, 9)
        assert distance == expected


class TestPoint3D:

    @pytest.mark.parametrize("point_name, expected", [("point_name",
                                                       "Point 2, 5, 8")])
    def test_string_method_class(self, point_name, expected):
        point = Point3D(2, 5, 8)
        point_name = point.__str__()
        assert point_name == expected

    @pytest.mark.parametrize("distance, expected", [("distance", 11.091)])
    def test_calculate_distance_beetwen_two_points(self, distance, expected):
        point = Point3D(3, 7, 12)
        distance = point.calculate_distance_beetwen_two_points(4, 8, 1)
        assert distance == expected


class TestWorker:
    pass
