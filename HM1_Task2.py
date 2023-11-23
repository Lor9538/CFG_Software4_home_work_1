import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print('Consider me implemented', perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


# Create instances
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(2, 3)
square = Square(4)

# Print results
print('Triangle Perimeter: ', triangle.calc_perimeter())
print('Rectangle Perimeter: ', rectangle.calc_perimeter())
print('Square Perimeter: ', square.calc_perimeter())
