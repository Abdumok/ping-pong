from turtle import Turtle
X_move=1
Y_move=1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=1
        self.y_move=1

    def move(self):
        self.goto(self.xcor()+ self.x_move, self.ycor()+ self.y_move)

    def bounce_from_wall(self):
        self.y_move *= -1

