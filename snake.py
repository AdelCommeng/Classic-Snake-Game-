from turtle import Screen,Turtle

SNAKES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    def createsnake(self):
        for position in SNAKES:
            self.add_segment(position)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]

    def move(self):
        for seq_sum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seq_sum - 1].xcor()
            new_y = self.segments[seq_sum - 1].ycor()
            self.segments[seq_sum].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
            if self.segments[0].heading() != DOWN:
                self.segments[0].setheading(UP)
    def down(self):
            if self.segments[0].heading() != UP:
                self.segments[0].setheading(DOWN)
    def left(self):
            if self.segments[0].heading() != RIGHT:
                self.segments[0].setheading(LEFT)
    def right(self):
            if self.segments[0].heading() != LEFT:
                self.segments[0].setheading(RIGHT)


