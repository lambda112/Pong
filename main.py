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
player_1 = Player(x = -355, y = 0)
player_2 = Player(x = 355, y = 0)
ball = Ball()

# Listen to Inputs
screen.listen()
screen.onkeypress(fun= player_1.upward, key = "Up")
screen.onkeypress(fun= player_1.downward, key = "Down")
screen.onkeypress(fun= player_2.upward, key = "w")
screen.onkeypress(fun= player_2.downward, key = "s")

# Game Loop
game_is_on = True
player_1_score = 0
player_2_score = 0

while game_is_on:
    # Inital Setup
    sleep(0.02)
    screen.update()
    ball.move()

    # Collision with Ceiling
    if ball.ycor() > 230 or ball.ycor() < -225:
        ball.bounce_y()

    # Collision with Paddle
    if ball.distance(player_2) < 80 and ball.xcor() > 350 and ball.movement_x > 0:
        ball.bounce_x()
    
    elif ball.distance(player_1) < 80 and ball.xcor() > -350 and ball.movement_x < 0:
        ball.bounce_x()

    # Check for Score
    if ball.xcor() > 380:
        ball.home()
        player_1_score += 1
        
    elif ball.xcor() < -380:
        ball.home()
        player_2_score += 1 

    print(f"Player1 {player_1_score}, Player2 {player_2_score}")


screen.exitonclick()


