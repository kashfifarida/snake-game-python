from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")    
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True 

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    #Detect the collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent() 
        score.increase()

    #Detect the collision with Wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detect colllision with tail.
    for segment in snake.segments[1:]:
      #if the head collids with the any segments in the tail.
      if snake.head.distance(segment) < 10:
          game_is_on = False
          score.game_over()
        #Trigger the GAME_OVER
    







screen.exitonclick()