from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "u")
screen.onkey(l_paddle.go_down, "d")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Needs to be bounce
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 80 and ball.xcor() > 320 or ball.distance(l_paddle) < 80 and ball.xcor() < -320:
        print("Made Contact")
        ball.bounce_x()

    #Detect the r_paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect the l_paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()


