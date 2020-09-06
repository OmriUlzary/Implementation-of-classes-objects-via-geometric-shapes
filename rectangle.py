from point import Point

class Rectangle:

    def __init__(self, length, width, start_point):
        self.length = length
        self.width = width
        self.start_point = start_point

    def __str__(self):
        if self.length > 0 and self.width > 0:
            return "Rectangle length: " + str(self.length) + " " "Rectangle width: " + " " + str(self.width) + " " + "Rectangle point: " + str(self.start_point)
        else:
            return "None"

    def get_area(self):
        if self.length > 0 and self.width > 0:
            return self.length * self.width
        else:
            return None

    def get_diag_length(self):
        if self.length > 0 and self.width > 0:
            return ((self.length ** 2) + (self.width ** 2)) ** 0.5
        else:
            return None

    def get_border_point(self):
        start_point = self.start_point
        point_2 = Point(self.width + self.start_point.x, self.start_point.y)
        point_3 = Point(self.start_point.x, self.start_point.y - self.length)
        point_4 = Point(self.width + self.start_point.x, self.start_point.y - self.length)
        border_list = [start_point, point_2, point_3, point_4]
        return border_list

    def add_value_height(self, value):
        self.length += value

    def add_value_width(self, value):
        self.width += value

