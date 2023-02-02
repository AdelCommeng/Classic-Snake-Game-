from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)
score=Scoreboard()
snake=Snake()
food=Food()
total_score=0

screen.listen()
#Buttons to play with
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.segments[0].distance(food)<15:
        score.score+=1
        food.refresh() #randomize the food location on canvas
        snake.extend()
        score.update_score()
    #detect colision with wall
    if snake.segments[0].xcor() >280 or snake.segments[0].xcor() <-299 or snake.segments[0].ycor() >285 or snake.segments[0].ycor() <-280:
        score.reset()
        snake.reset()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <10:
            score.reset()
            snake.reset()


screen.exitonclick()

