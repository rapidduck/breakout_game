from turtle import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(310, 190)
        self.score = 0
        self.add_score(0)

    def add_score(self, score):
        self.clear()
        self.score += score
        self.write(f"Score: {self.score}", font=("Times New Roman", 20), align="right")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nfinal score: {self.score}", font=("Times New Roman", 30, "bold"), align="center")