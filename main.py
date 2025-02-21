from turtle import Screen
from paddle import Paddle
from net import Net
from ball import Ball
from scoreboard import Score
import time

#Setup Main Screen
window = Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.title('Ping Pong v1.00')
window.tracer(0)


# Create Net:
net= Net()
# Create Ball:
ball= Ball()

#Add players name:
player1= window.textinput(title="Player1", prompt="Enter your name: ")
player2= window.textinput(title="Player2", prompt="Enter your name: ")

# Create Score:
r_score= Score( position=(200, 280), name=player1 )
l_score= Score( position=(-200, 280), name=player2 )

# Create Paddles:
r_paddle= Paddle(position=(370, 0))
l_paddle= Paddle(position=(-380, 0))

# Control Paddle move:
window.listen()
window.onkey(fun=r_paddle.go_up, key="Up")
window.onkey(fun=r_paddle.go_down, key="Down")

window.onkey(fun=l_paddle.go_up, key="w")
window.onkey(fun=l_paddle.go_down, key="s")


game_on= True
while game_on:
    ball.move()
    # Detect collision with wall:
    if (ball.ycor() > 280) or (ball.ycor()< -270):
        ball.bounce_from_wall()

    # Detect collision right paddle:
    elif (ball.xcor() > 340) and (r_paddle.distance(ball) <= 50):
        ball.bounce_from_paddle()

    # Detect collision left paddle:
    elif (ball.xcor() < -350) and (l_paddle.distance(ball) <= 50):
        ball.bounce_from_paddle()

    # If the Right paddle miss the ball:
    if ball.xcor() > 420:
        ball.goto(0,0)
        l_score.increase()

    # if the left paddle miss the ball:
    elif ball.xcor() < -420:
        ball.goto(0, 0)
        r_score.increase()


    time.sleep(0.005)
    window.update()



window.exitonclick()