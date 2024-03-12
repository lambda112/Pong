import turtle as t
from player import Player
from ball import Ball
from time import sleep

# Setup Screen
screen = t.Screen()
screen.setup(width=800, height=500)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Create Dotted Line in Middle of Screen
dotted_line = t.Turtle("square")
dotted_line.color("white")
dotted_line.shapesize(stretch_len=0.2, stretch_wid=1)
dotted_line.penup()
dotted_line.hideturtle()
dotted_line.goto(x = 0, y = 250)

for i in range(30):
    dotted_line.pendown()
    dotted_line.goto(x = 0, y = dotted_line.ycor() - 21.5)
    dotted_line.penup()
    dotted_line.goto(x = 0, y = dotted_line.ycor() - 21.5)

# Create Instances
player_1 = Player()
player_1.player.goto(x = 355, y = 0)
player_2 = Player()
player_2.player.goto(x = -363, y = 0)
ball = Ball()

# Listen to Inputs
screen.listen()
screen.onkeypress(fun= player_1.upward, key = "w")
screen.onkeypress(fun= player_1.downward, key = "s")
screen.onkeypress(fun= player_2.upward, key = "Up")
screen.onkeypress(fun= player_2.downward, key = "Down")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    sleep(0.02)

screen.exitonclick()


