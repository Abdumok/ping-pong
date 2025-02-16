from turtle import Screen
from paddle import Paddle
from net import Net

#Setup Main Screen
window = Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.title('Ping Pong v1.00')
window.tracer(0)


# Create Paddle:
r_paddle= Paddle(position=(370, 0))
l_paddle= Paddle(position=(-380, 0))

# Create Net:
net= Net()

game_on= True
while game_on:


    window.update()



window.exitonclick()