from turtle import *

STAMP_SIZE = 20

class Block(Turtle):

    def __init__(self, x, y, width, color, score):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color(color)
        self.score = score
        self.penup()
        self.shapesize(40 / STAMP_SIZE, width / STAMP_SIZE)
        self.goto(x, y)