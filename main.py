from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

# Makes paddle spawn at respective spot instead of center of screen
screen.tracer(0)

# Create Paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
scoreboard = Scoreboard()

# Paddle Movement
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor () > 320:
        ball.bounce_x()
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor () < -320:
        ball.bounce_x()
        ball.bounce_y()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


