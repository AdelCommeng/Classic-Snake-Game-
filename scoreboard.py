from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.pendown()
        self.write(f"Score:{self.score}",align="center",font=('Arial', 13, 'normal'))
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", align="center", font=('Arial', 13, 'normal'))

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align="center", font=('Arial', 13, 'normal'))
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_score()