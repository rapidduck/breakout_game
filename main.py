import time
from turtle import *
from player import Player
from game_ball import Ball
from block import Block
from scoreboard import Scoreboard

screen = Screen()
screen.setup(700, 500)
screen.tracer(0, 0)
screen.bgcolor("gray")

class GameEdge(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("#404040")
        self.penup()


left_wall = GameEdge()
left_wall.shapesize(500 / 20, 20 / 20)
left_wall.goto(-340, 0)

top_wall = GameEdge()
top_wall.shapesize(20 / 20, 780 / 20)
top_wall.goto(0, 240)

right_wall = GameEdge()
right_wall.shapesize(500 / 20, 20 / 20)
right_wall.goto(331, 0)

player = Player()
ball = Ball()

all_turtles = [left_wall, top_wall, right_wall, player]

colors = "red", "yellow", "blue"
scores = 1, 3, 5
WIDTH = 54.78
SPACE = WIDTH / 6
total_score = 0
for color in colors:
    for i in range(10):
        block = Block(x=-293 + i*(WIDTH + SPACE), y=colors.index(color)*50, width=WIDTH,
                      color=color, score=scores[colors.index(color)])
        total_score += block.score
        all_turtles.append(block)

scoreboard = Scoreboard()

while True:
    time.sleep(0.00001 * (1000 - scoreboard.score))
    player.follow_mouse(screen)
    ball.check_for_collisions(all_turtles, scoreboard)
    ball.move()
    if ball.pos()[1] < -250:
        break
    if scoreboard.score >= total_score:
        break
    screen.update()

scoreboard.game_over()
screen.exitonclick()