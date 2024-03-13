from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.movement_x = 5
        self.movement_y = 5

    def move(self):
        new_x = self.xcor() + self.movement_x
        new_y = self.ycor() + self.movement_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.movement_y = self.movement_y * -1

    def bounce_x(self):
        self.movement_x = self.movement_x * -1

            