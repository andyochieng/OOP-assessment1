class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def calculate_area(self):
        return self.length * self.width

square = Rectangle(5)
print("Square Area:", square.calculate_area())

rectangle = Rectangle(5, 10)
print("Rectangle Area:", rectangle.calculate_area())