import turtle as t
from player import Player

# Setup Screen
screen = t.Screen()
screen.setup(width=800, height=500)
screen.title("Pong")
screen.bgcolor("black")

# Create Instances
player_1 = Player()
player_2 = Player()

# Listen to Inputs
screen.listen()
screen.onkeypress(fun= player_1.upward, key = "w")
screen.onkeypress(fun= player_1.downward, key = "s")



screen.exitonclick()


