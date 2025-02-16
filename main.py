from turtle import Screen
from paddle import Paddle
from net import Net
from ball import Ball
import time

#Setup Main Screen
window = Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.title('Ping Pong v1.00')
window.tracer(0)


# Create Paddle:
r_paddle= Paddle(position=(370, 0))
l_paddle= Paddle(position=(-380, 0))

# Control Paddle move:
window.listen()
window.onkey(fun=r_paddle.go_up, key="Up")
window.onkey(fun=r_paddle.go_down, key="Down")

window.onkey(fun=l_paddle.go_up, key="w")
window.onkey(fun=l_paddle.go_down, key="s")



# Create Net:
net= Net()
# Create Ball:
ball= Ball()

game_on= True
while game_on:
    ball.move()

    time.sleep(0.001)
    window.update()



window.exitonclick()