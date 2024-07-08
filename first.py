from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_ison=True
while game_ison:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect food colision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #colison with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()< -295:
        game_ison=False
        scoreboard.gameover()
    #detect tail colison
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_ison=False
            scoreboard.gameover()

screen.exitonclick() 