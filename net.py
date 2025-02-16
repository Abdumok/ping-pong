from turtle import Turtle

class Net():
    def __init__(self):
        self.net= []
        self.create_net()

    def create_net(self):
        for i in range(8):
            new_net = Turtle()
            new_net.color("white")
            new_net.shape("square")
            new_net.shapesize(stretch_len=0.3, stretch_wid=2)
            new_net.penup()
            new_net.goto(0, (280-80*i))
            self.net.append(new_net)