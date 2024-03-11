import turtle as t
from player import Player

# Setup Screen
screen = t.Screen()
screen.setup(width=800, height=500)
screen.title("Pong")
screen.bgcolor("black")

# Create Instances
player_1 = Player()
player_1.player.goto(x = 355, y = 0)
player_2 = Player()
player_2.player.goto(x = -363, y = 0)

# Listen to Inputs
screen.listen()
screen.onkeypress(fun= player_1.upward, key = "w")
screen.onkeypress(fun= player_1.downward, key = "s")
screen.onkeypress(fun= player_2.upward, key = "Up")
screen.onkeypress(fun= player_2.downward, key = "Down")

# Game Loop


screen.exitonclick()


