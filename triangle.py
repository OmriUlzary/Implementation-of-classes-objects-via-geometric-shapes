from point import Point

class Triangle:

    def __init__(self, points_list):
        self.points_list = points_list
        
    def __str__(self):
        return "The Three points of the triangle are: " + str(self.points_list[0]) + "," + str(self.points_list[1]) + "," + str(self.points_list[2])

    def add_value_x(self, index, value):
        self.points_list[index].x += value

    def add_value_y(self, index, value):
        self.points_list[index].y += value

    def get_edges_length(self):
        length_0 = self.points_list[0].get_distance(self.points_list[1].x, self.points_list[1].y)
        length_1 = self.points_list[0].get_distance(self.points_list[2].x, self.points_list[2].y)
        length_2 = self.points_list[1].get_distance(self.points_list[2].x, self.points_list[2].y)
        edges_length_list = [length_0, length_1, length_2]
        return edges_length_list

    def get_height(self):
        m = (self.points_list[2].y - self.points_list[1].y) / (self.points_list[2].x - self.points_list[1].x)
        b = self.points_list[1].y - (m * self.points_list[1].x)
        top = m * self.points_list[0].x - self.points_list[0].y + b
        bottom = (m ** 2 + 1) ** 0.5
        return abs(top / bottom)

    def get_area(self):
        base = self.points_list[1].get_distance(self.points_list[2].x, self.points_list[2].y)
        height = self.get_height()
        return (height * base) / 2

