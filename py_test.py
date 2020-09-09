import pytest

from animal import (Point2D,
                    Point3D,
                    Worker,
                    Manager,
                    DataAnalytics,
                    Programmer,
                    SeniorProgrammer)


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
        assert point.calculate_distance_beetwen_two_points(x, y, z) == expected


class TestWorker:

    @pytest.mark.parametrize("expected, kwargs", [(
        """Programmer John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"position": "p", "first_name": "John", "last_name": "Doe", "gender": "m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        worker = Worker(**kwargs)
        assert str(worker) == expected

    @pytest.mark.parametrize(
        "key,value",
        [
            ("gender", "bbbb"),
            ("gender", "f"),
            ("salary", "hundred"),
            ("salary", -2000),
            ("level", "three"),
            ("level", -9)
        ]
    )
    def test_instantiation_of_class(self, key, value):
        with pytest.raises(ValueError):
            Worker(key=value)

    def test_level_up_workers_level(self):
        worker = Worker(position="p", gender='f', level=1)
        worker.level_up_workers_level()
        worker.level_up_workers_level()
        assert worker.level == 3

    def test_increase_workers_salary_when_value_and_percentage(self):
        with pytest.raises(ValueError):
            worker = Worker(position='p', gender='f')
            worker.increase_workers_salary(percentage=0.2, value=2500)

    def test_increase_workers_salary_when_value(self):
        worker = Worker(position='s', gender='f', salary=100)
        worker.increase_workers_salary(value=14)
        assert worker.salary == 114

    def test_increase_workers_salary_when_percentage(self):
        worker = Worker(position='m', gender='f', salary=100)
        worker.increase_workers_salary(percentage=0.05)
        assert worker.salary == 105

    def test_increase_workers_salary_when_percentage_is_not_float(self):
        with pytest.raises(TypeError):
            worker = Worker(position='p', gender='f', salary=100)
            worker.increase_workers_salary(percentage='five')

    def test_increase_workers_salary_when_value_is_not_int(self):
        with pytest.raises(TypeError):
            worker = Worker(position='m', gender='m', salary=200)
            worker.increase_workers_salary(percentage=2)


class TestManager:

    @pytest.mark.parametrize("expected, kwargs", [(
        """Manager John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"position": "m", "first_name": "John", "last_name": "Doe", "gender": "m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        manager = Manager(**kwargs)
        assert str(manager) == expected

    def test_set_salary_to_worker(self):
        worker = Programmer(position='p', gender='f')
        manager = Manager(position='m', gender='m')
        manager.set_salary_to_worker(worker=worker, salary_value=150)
        assert worker.salary == 150


class TestDataAnalytics:

    @pytest.mark.parametrize("expected, kwargs", [(
        """Data Analytics John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"position": "d", "first_name": "John", "last_name": "Doe", "gender": "m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        data_analytics = DataAnalytics(**kwargs)
        assert str(data_analytics) == expected

    @pytest.mark.parametrize(
        "data_type, value",
        [
            ("data_type", 'bbb'),
            ("data_type", "list")
        ]
    )
    def test_create_and_return_data_when_data_type_incorrect(
            self, data_type, value):
        with pytest.raises(ValueError):
            data_analytics = DataAnalytics(position='d',gender='f')
            data_analytics.create_and_return_data(data_type=value)

    def test_create_and_return_data_when_data_type_list(self):
        data_analytics = DataAnalytics(position='d', gender='m')
        list_data = data_analytics.create_and_return_data(data_type='l')
        assert isinstance(list_data, list)

    def test_create_and_return_data_when_data_type_dict(self):
        data_analytics = DataAnalytics(position='d', gender='m')
        dict_data = data_analytics.create_and_return_data(data_type='d')
        assert isinstance(dict_data, dict)


class TestProgrammer:

    @pytest.mark.parametrize("expected, kwargs", [(
        """Programmer John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"position": "p", "first_name": "John", "last_name": "Doe", "gender": "m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        programmer = Programmer(**kwargs)
        assert str(programmer) == expected

    def test_if_programmer_do_programming(self):
        programmer = Programmer(position='p', gender='f')
        html_code = programmer.do_programming()
        assert html_code == '<p> look my code is awsome </p>'


class TestSeniorProgrammer:

    @pytest.mark.parametrize("expected, kwargs", [(
        """Senior Programmer John Doe,
                salary: 0,
                level: 0,
                gender: m""",
        {"position": "s", "first_name": "John", "last_name": "Doe", "gender": "m"})
        ])
    def test_string_method_class(self, expected, kwargs):
        programmer = SeniorProgrammer(**kwargs)
        assert str(programmer) == expected

    def test_if_programmer_do_programming(self):
        programmer = SeniorProgrammer(position='d', gender='f')
        html_code = programmer.do_programming()
        assert html_code == '<p> look my code is awsome </p>'
