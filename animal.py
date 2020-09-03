import unittest

# 1
# Write a class representing a 2D point: Point2D. Constructor should have two
# arguments x, y define a _str_ method for that class
# write a method calculating a distance between two points


class Point2D:
    """
    class describing point has x and y coordinates
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"Point {self.x}, {self.y}")

    def calculate_distance_beetwen_two_points(self, x, y):
        """
        calculate distance beetwen two points
        """
        return (
            f"Distance beetwen two points is {self.x - x}x and {self.y - y}y")


class TestPoint2D(unittest.TestCase):

    def setUp(self):
        self.point = Point2D(3, 5)

    def test_string_method_of_instance(self):
        self.assertEqual("Point 3, 5", self.point.__str__())

    def test_calculate_distance_beetwen_two_points(self):
        self.assertEqual(
            "Distance beetwen two points is 1x and 2y",
            self.point.calculate_distance_beetwen_two_points(2, 3))

# Write a class which inherits from Print2D class and implements 3D point,
# the arguments should be x, y, z write a _str_ method for that class
# (you can use super) write a method calculating a distance between two points


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{super().__str__()}, {self.z}"

    def calculate_distance_beetwen_two_points(self, x, y, z):
        """
        calculate distance beetwen two points
        """
        return (f"""Distance beetwen two points is
                {self.x - x}x {self.y - y}y {self.z -z}z""")


class TestPoint3D(unittest.TestCase):

    def setUp(self):
        self.point = Point3D(2, 8, 5)

    def test_string_method_of_instance(self):
        self.assertEqual("Point 2, 8, 5", self.point.__str__())

    def test_calculate_distance_beetwen_two_points(self):
        self.assertEqual(
                        """Distance beetwen two points is
                1x 7y 4z""",
                        self.point.calculate_distance_beetwen_two_points(
                            1, 1, 1))

# 3
# Write a Worker class which will take first_name, last_name, salary, level
# and gender write a _str_ and _init_ methods. Add method to level up and a
# method to increase salary by some value or percentage use inheritance and
# write a Manager, DataAnalytics, Programmer and SeniorProgrammer write a
# method in Manager class to set salary for others write a method
# do_programming for programmers which will return some HTML code in string
# write a method which will return some data in a list od dictionaries for
# data scientist


class Worker:

    GENDER = ['f', 'm', 'n']

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.salary = kwargs.get('salary', 0)
        if not isinstance(self.salary, int):
            raise ValueError("worker's salary has to be an integer")
        elif isinstance(self.salary, int) and self.salary < 0:
            raise ValueError("worker's salary has to be a positive integer")
        self.level = kwargs.get('level', 0)
        if not isinstance(self.level, int):
            raise ValueError("worker's level has to be integer")
        elif isinstance(self.level, int) and self.level < 0:
            raise ValueError("worker's level has to be positive integer")
        self.gender = kwargs.get('gender', '')
        if self.gender.lower() not in self.GENDER:
            raise ValueError(
                "worker's gender can be only f-female, m-male, n-non binary")

    def __str__(self):
        return f"""{self.first_name} {self.last_name},
                salary: {self.salary},
                level: {self.level},
                gender: {self.gender}"""

    def level_up_workers_level(self):
        self.level += 1
        return abs(self.level)

    def increase_workers_salary(self, value=None, percentage=None):
        if value is not None and percentage is not None:
            raise ValueError(
                "You have to choose or value or percentage to increase salary")
        elif value is not None and percentage is None:
            self.salary += value
        else:
            self.salary = self.salary + self.salary * percentage
        return self.salary


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


class Manager(Worker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""


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


class DataAnalytics(Worker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""


class Programmer(Worker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""


class SeniorProgrammer(Worker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""


if __name__ == "__main__":
    unittest.main()
