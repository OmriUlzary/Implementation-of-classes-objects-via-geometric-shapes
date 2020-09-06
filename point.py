class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist_zero = self.get_distance(0, 0)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_distance(self, x1, y1):
        delta_x = (self.x - x1) ** 2
        delta_y = (self.y - y1) ** 2
        return (delta_x + delta_y) ** 0.5

    def add_value_x(self, value):
        self.x += value

    def add_value_y(self, value):
        self.y += value


