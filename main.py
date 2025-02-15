from turtle import Screen
from paddle import Paddle

#Setup Main Screen
window = Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.title('Ping Pong v1.00')


# Create Paddle:
r_paddle= Paddle(position=(370, 0))
l_paddle= Paddle(position=(-380, 0))




window.exitonclick()