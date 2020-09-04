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

    @pytest.mark.parametrize("x, y, z, expected", [(4, 8, 1, 11.091)])
    def test_calculate_distance_beetwen_two_points(self, x, y, z, expected):
        point = Point3D(3, 7, 12)
        #  distance = point.calculate_distance_beetwen_two_points(4, 8, 1)
        assert point.calculate_distance_beetwen_two_points(x,y,z) == expected


class TestWorker:

    @pytest.mark.parametrize("expected, kwargs", [(
        """John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"first_name":"John", "last_name":"Doe", "gender":"m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        worker = Worker(**kwargs)
        assert str(worker) == expected
    
    def test_instance_of_class_error_when_gender_wrong(self):
        with pytest.raises(ValueError):
            worker = Worker(gender='bbbb')
    
    def test_instance_creation_of_class_fail_of_correct_variable(self):
        with pytest.raises(ValueError):
            worker = Worker(gender='f')
    
    def test_instance_creation_of_class_when_salary_not_int(self):
        with pytest.raises(ValueError):
            worker = Worker(salary="hundred")

    def test_instance_creation_of_class_when_salary_negativ_int(self):
        with pytest.raises(ValueError):
            worker = Worker(salary=-(2000))

