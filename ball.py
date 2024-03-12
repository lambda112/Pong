from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.movement_x = 5
        self.movement_y = 5
        self.player1_points = 0
        self.player2_points = 0

    def move(self):
        self.collision()

        if self.goal_scored():
            self.player1_points += 1
        elif self.goal_scored() == False:
            self.player2_points += 1

        new_x = self.xcor() + self.movement_x
        new_y = self.ycor() + self.movement_y
        self.goto(new_x, new_y)
        print(f"{self.player1_points=}{self.player2_points=}")

    def collision(self):
        if self.ycor() > 230 or self.ycor() < -225:
            if self.movement_y > 0: 
                self.movement_y = -self.movement_y

            elif self.movement_y < 0:
                self.movement_y = 5

    def goal_scored(self):
        if self.xcor() > 380:
            self.home()
            return 1
        
        elif self.xcor() > 380:
            self.home()
            return 0
        
        else:
            return None
            