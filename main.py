from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('snejk kowera')
screen.tracer(0)
startowe = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game = True
while game:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.segments[0].distance(food) < 19:
        food.travel()
        scoreboard.point()
        snake.extend()

    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -295:
        scoreboard.gameover()
        game = False

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
            game = False
            scoreboard.gameover()



screen.exitonclick()
