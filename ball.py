"""
Create ball and make it move

width = 20
height = 20
x_pos = 0
y_pos = 0
"""
from turtle import Turtle

class Ball(Turtle):

    # Initiate ball
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # Used for bounce()
        self.x_move = 10
        self.y_move = 10

    # Spawn ball with movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    # Detect collision with wall
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # Reset ball position
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()




