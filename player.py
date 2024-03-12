from turtle import Turtle
Y_BOUND = 200

class Player():
    def __init__(self) -> None:
        self.player = Turtle(shape="square")
        self.player.color("white")
        self.player.shapesize(stretch_len=1,stretch_wid=5)
        self.player.penup()

    def upward(self) -> None:
        if self.player.ycor() < Y_BOUND:
            self.player.sety(self.player.ycor() + 20)
            return True
        
        return False
    
    def downward(self) -> None:
        if self.player.ycor() > -Y_BOUND:
            self.player.sety(self.player.ycor() - 20)
            return True
        
        return False
    