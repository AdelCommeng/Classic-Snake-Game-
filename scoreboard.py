from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        #Save the highest score into a file so when you play the game another day, the highest score will show up
        with open("data.txt") as file:
            content=(file.read())
        self.highscore=int(content)
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
            self.highscore = self.score
        #Save the highest score into a file
        with open("data.txt", mode="w") as data:
            updated = int(data.write(f"{self.highscore}"))

        self.score=0
        self.update_score()

