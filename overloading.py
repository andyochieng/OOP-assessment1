class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(8, 2)
vector2 = Vector(7, 3)

result = vector1 + vector2
print("Result of vector addition:", result)
