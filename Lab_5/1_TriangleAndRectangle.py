class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle(Shape):

    def area(self):
        return self.x * self.y * 0.5


class Rectangle(Shape):

    def area(self):
        return self.x * self.y


if __name__ == "__main__":
    t = Triangle(1, 1)
    print(t.area())
    r = Rectangle(1, 1)
    print((r.area()))
