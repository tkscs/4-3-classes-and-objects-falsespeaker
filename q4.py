import turtle

# Define the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.dot()
        # Optional extra credit: label the point
        turtle.write(str(self), align="left")


# Setup turtle
turtle.penup()

# Create 4 Point objects
p1 = Point(0, 0)
p2 = Point(100, 0)
p3 = Point(100, 100)
p4 = Point(0, 100)

# Print the objects
print(p1)
print(p2)
print(p3)
print(p4)

# Draw the points
p1.draw()
p2.draw()
p3.draw()
p4.draw()

# Keep window open
turtle.done()