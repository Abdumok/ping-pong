from turtle import Turtle

PADDLE_SPEED= 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)