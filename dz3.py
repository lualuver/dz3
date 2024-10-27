class Rectangle:
    def __init__(self, height=5, width=10):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(15, 20)
rectangle3 = Rectangle(width=55)
rectangle4 = Rectangle()

print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())
