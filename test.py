import unittest

from animal import Point2D, Point3D, Programmer, Worker, Manager, DataAnalytics


class TestPoint2D(unittest.TestCase):

    def setUp(self):
        self.point = Point2D(3, 5)

    def test_string_method_of_instance(self):
        self.assertEqual("Point 3, 5", self.point.__str__())

    def test_calculate_distance_beetwen_two_points(self):
        self.assertEqual(
            2.236,
            self.point.calculate_distance_beetwen_two_points(2, 3))


class TestPoint3D(unittest.TestCase):

    def setUp(self):
        self.point = Point3D(2, 8, 5)

    def test_string_method_of_instance(self):
        self.assertEqual("Point 2, 8, 5", self.point.__str__())

    def test_calculate_distance_beetwen_two_points(self):
        self.assertEqual(
                        8.124,
                        self.point.calculate_distance_beetwen_two_points(
                            1, 1, 1))


class TestWorker(unittest.TestCase):

    def setUp(self):
        self.worker = Worker(first_name='John',
                             last_name='Paul',
                             salary=140,
                             level=1,
                             gender='M')

    def test_string_method_worker_instance(self):
        self.assertEqual(
"""John Paul,
                salary: 140,
                level: 1,
                gender: M""",
            self.worker.__str__()
             )

    def test_raises_error_salary_is_not_integer_when_init(self):
        with self.assertRaises(ValueError):
            self.worker.__init__(salary='hundred')

    def test_raises_error_salary_is_integer_lower_then_0_when_init(self):
        with self.assertRaises(ValueError):
            self.worker.__init__(salary=(-5200))

    def test_raises_error_level_is_not_integer_when_init(self):
        with self.assertRaises(ValueError):
            self.worker.__init__(level='one')

    def test_raises_error_level_is_not_positive_int_when_init(self):
        with self.assertRaises(ValueError):
            self.worker.__init__(level=(-99))

    def test_raises_error_gender_is_not_GENDER_choice_when_init(self):
        with self.assertRaises(ValueError):
            self.worker.__init__(gender='man')

    def test_increase_workers_salary_when_value(self):
        self.worker.increase_workers_salary(2000)
        self.assertEqual(2140, self.worker.salary)

    def test_increase_workers_salary_when_percentage(self):
        self.worker.increase_workers_salary(percentage=0.1)
        self.assertEqual(154, self.worker.salary)

    def test_increase_workers_salary_when_value_and_percentage(self):
        with self.assertRaises(ValueError):
            self.worker.increase_workers_salary(value=100, percentage=0.2)

    def test_level_up_two_times_worker(self):
        self.worker.level_up_workers_level()
        self.worker.level_up_workers_level()
        self.assertEqual(3, self.worker.level)


class TestManager(unittest.TestCase):

    def setUp(self):
        self.manager = Manager(first_name='Harry',
                               last_name='Potter',
                               salary=250,
                               level=3,
                               gender='M')

    def test_string_method(self):
        self.assertEqual(
"""Manager Harry Potter,
                salary: 250,
                level: 3,
                gender: M""",
                self.manager.__str__())

    def test_set_salary_to_worker(self):
        worker = Worker(gender='m')
        self.manager.set_salary_to_worker(worker, 100)
        self.assertEqual(100, worker.salary)

    def test_set_salary_to_programmer(self):
        programmer = Programmer(gender='f')
        self.manager.set_salary_to_worker(programmer, 500)
        self.assertEqual(500, programmer.salary)


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer(first_name='Anne',
                                     last_name='Doe',
                                     salary=250,
                                     level=0,
                                     gender='f')

    def test_do_programming(self):
        code = self.programmer.do_programming()
        self.assertEqual("<p> look my code is awsome </p>", code)


class TestDataAnalitycs(unittest.TestCase):

    def setUp(self):
        self.data_analytics = DataAnalytics(
            firste_name='Paul',
            last_name='Smith',
            level=2,
            salary=400,
            gender='m'
        )

    def test_create_and_return_data_if_not_valid(self):
        with self.assertRaises(ValueError):
            self.data_analytics.create_and_return_data('sh')

    def test_create_and_return_data_as_list(self):
        created_list = self.data_analytics.create_and_return_data('l')
        self.assertIsInstance(created_list, list)

    def test_create_and_return_data_as_dictionary(self):
        created_dict = self.data_analytics.create_and_return_data('d')
        self.assertIsInstance(created_dict, dict)


if __name__ == "__main__":
    unittest.main()
