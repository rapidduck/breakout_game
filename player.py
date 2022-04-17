from turtle import *

STAMP_SIZE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(20 / STAMP_SIZE, 200 / STAMP_SIZE)
        self.goto(0, -200)

    def follow_mouse(self, screen):
        canvas = screen.getcanvas()
        x = canvas.winfo_pointerx() - canvas.winfo_rootx() - 350
        if x >= 220:
            x = 220
        elif x <= -229:
            x = -229
        self.goto(x, self.ycor())
