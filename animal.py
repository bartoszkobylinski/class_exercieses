from math import sqrt

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
        distance = round(sqrt((y -self.y)**2 +(self.x - x)**2), 3)
        return distance

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
        distance = round(sqrt((x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2), 3)
        return distance

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

    def increase_workers_salary(self, value=None, percentage=None):
        if value is not None and percentage is not None:
            raise ValueError(
                "You have to choose or value or percentage to increase salary")
        elif value is not None and percentage is None:
            self.salary += value
        else:
            self.salary = self.salary + self.salary * percentage


class Manager(Worker):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""

    def set_salary_to_worker(self, worker, salary_value):
        worker.salary = salary_value


class DataAnalytics(Worker):

    DATA_TYPE = ['l', 'd']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""

    def create_and_return_data(self, data_type):
        if data_type not in self.DATA_TYPE:
            raise ValueError("""You can choose two data types:
                             l - list
                             d - dictionaries""")
        elif data_type == "l":
            return ['some data', 'data']
        else:
            return {'somy_key': 'some_value'}


class SoftwareDeveloper:

    def do_programming(self):
        return"<p> look my code is awsome </p>"


class Programmer(Worker, SoftwareDeveloper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""


class SeniorProgrammer(Worker, SoftwareDeveloper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = __class__.__name__

    def __str__(self):
        worker_str = super().__str__()
        return f"""{self.position} {worker_str}"""
