from point import Point
import math

class Circle:

    def __init__(self, center_point, radius):
        self.center_point = center_point
        self.radius = radius

    def __str__(self):
        if self.radius > 0:
            return "(X-" + str(self.center_point.x) + ")^2+" + "(Y-" + str(self.center_point.y) + ")^2= " + str(
                    self.radius ** 2)
        else:
            return "None"

    def get_area(self):
        if self.radius > 0:
            return math.pi * (self.radius ** 2)
        else:
            return None

    def get_circumence(self):
        if self.radius > 0:
            return 2 * math.pi * self.radius
        else:
            return None

    def is_contains_point(self, x, y):
        if self.radius > 0:
            return (x - self.center_point.x) ** 2 + (y - self.center_point.y) ** 2 <= self.radius ** 2
        else:
            return None

