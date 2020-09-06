from point import Point
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

rectangle_list = []
triangle_list = []
circle_list = []

def get_point_from_user():
    x = float(input("Please enter x value"))
    y = float(input("Please enter y value"))
    return Point(x, y)

while True:
    print("Welcome! Please choose an option:")
    print("(0) - Exit")
    print("(1) - Add Rectangle")
    print("(2) - Add Triangle")
    print("(3) - Add Circle")
    print("(4) - Get Biggest Rectangle")
    print("(5) - Change X Coordinates")
    print("(6) - Check Is Contains")

    choice = int(input())

    if choice == 0:
        print("Bye Bye")
        break

    elif choice == 1:
        length = float(input(("Please enter length")))
        width = float(input("please enter width"))
        if length > 0 and width > 0:
            point = get_point_from_user()
            rectangle = Rectangle(length, width, point)
            rectangle_list.append(rectangle)
            print("The Rectangle", rectangle, "added successfully!")
        else:
            print("Please Enter positive numbers")

    elif choice == 2:
        point_0 = get_point_from_user()
        point_1 = get_point_from_user()
        point_2 = get_point_from_user()
        triangle = Triangle([point_0, point_1, point_2])
        triangle_list.append(triangle)
        print("The Triangle", triangle, "added successfully")

    elif choice == 3:
        center_point = get_point_from_user()
        radius = float(input("Please enter radius"))
        if radius > 0:
            circle = Circle(center_point, radius)
            circle_list.append(circle)
            print("The Circle", circle, "added successfully")
        else:
            print("Please Enter positive radius")

    elif choice == 4:
        max_area = 0
        max_rectangle = None
        for rectangle in rectangle_list:
            area = rectangle.get_area()
            if area > max_area:
                max_area = area
                max_rectangle = rectangle
        print(max_rectangle)

    elif choice == 5:
        value = float(input("Please enter value"))
        for rectangle in rectangle_list:
            rectangle.start_point.add_value_x(value)
        for triangle in triangle_list:
            triangle.points_list[0].add_value_x(value)
            triangle.points_list[1].add_value_x(value)
            triangle.points_list[2].add_value_x(value)
        for circle in circle_list:
            circle.center_point.add_value_x(value)

    elif choice == 6:
        point = get_point_from_user()
        index = int(input("Please enter index"))
        circle = circle_list[index]
        result = circle.is_contains_point(point.x, point.y)
        print(result)
