from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,True,"center",("Arial",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,True,"center",("Arial",80,"normal"))

    def score_r(self):
        self.r_score+=1
        self.update_scoreboard()
    def score_l(self):
        self.l_score+=1
        self.update_scoreboard()
