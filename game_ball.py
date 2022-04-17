import math
import random
import turtle
from turtle import *
from block import Block

STAMP_SIZE = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.last_collision_object = None
        self.last_distance_with_collision_object = None
        self.last_collisions = [None, None, None]
        self.shape("circle")
        self.speed("normal")
        self.color("red")
        self.penup()
        self.shapesize(20 / STAMP_SIZE, 20 / STAMP_SIZE)
        self.goto(0, -100)
        self.setheading(30)

    def check_for_collisions(self, all_turtles, scoreboard):
        for turtle in all_turtles:
            if turtle == self.last_collision_object:
                continue
            height, width, useless = turtle.shapesize()
            diff_factor_is_width = True
            if width > height:
                diff_factor_is_width = False

            if diff_factor_is_width:
                diff = abs(abs(self.xcor()) - abs(turtle.xcor()))
            else:
                diff = abs(abs(self.ycor()) - abs(turtle.ycor()))

            if diff < 20:
                a = (width * 20 + 10) ** 2
                b = (height * 20 + 10) ** 2
                acceptable_distance = math.sqrt(a + b) / 2

                distance = self.distance(turtle)

                if distance <= acceptable_distance:
                    print(f"BOUNCE")
                    if turtle != self.last_collision_object:
                        if type(turtle) == Block:
                            scoreboard.add_score(turtle.score)
                            turtle.goto(10000,10000)
                        self.last_collision_object = turtle
                        self.last_distance_with_collision_object = distance
                        self.set_new_heading()
                    else:
                        self.set_new_heading()
                        self.setheading(self.heading() + 180)
                        self.last_collision_object = None

    def set_new_heading(self):
        new_heading = self.heading() + random.randint(150, 225)
        self.setheading(new_heading)

    def move(self):
        self.forward(5)

