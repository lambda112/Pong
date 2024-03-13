from turtle import Turtle
Y_BOUND = 200

class Player(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def upward(self) -> None:
        if self.ycor() < Y_BOUND:
            self.sety(self.ycor() + 20)
            return True
        
        return False
    
    def downward(self) -> None:
        if self.ycor() > -Y_BOUND:
            self.sety(self.ycor() - 20)
            return True
        
        return False
    