from turtle import Turtle

class Score(Turtle):
    def __init__(self, position, name):
        super().__init__()
        self.score= 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.name= name
        self.write_score()

    def write_score(self):
        self.write(f"{self.name} | Score: {self.score}", font=("courier", 12, "bold"), align="center")

    def increase(self):
        self.clear()
        self.score += 1
        self.write_score()
