from turtle import Turtle

class Player():
    def __init__(self) -> None:
        self.player = Turtle(shape="square")
        self.player.color("white")
        self.player.shapesize(stretch_len=0.7,stretch_wid=4)
        self.player.penup()

    def upward(self) -> None:
        self.player.sety(self.player.ycor() + 20)
    
    def downward(self) -> None:
        self.player.sety(self.player.ycor() - 20)
    