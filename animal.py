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
                        "Distance beetwen two points is 1x 7y 4z",
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

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.salary = kwargs.get('salary', 0)
        self.level = kwargs.get('level', 0)
        self.gender = kwargs.get('gender', '')


if __name__ == "__main__":
    unittest.main()
