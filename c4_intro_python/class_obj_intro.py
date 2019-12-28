class Rectangle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


a = Rectangle(1, "red")
print(a)
print(a.radius)
print(a.color)
print(dir(a))
