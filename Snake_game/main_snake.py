from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from os import system
import time


system("cls")

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Ed Snake Game")
my_screen.tracer(0)




snake_game = Snake()
my_food = Food()
scoreboard = Scoreboard()

# Snake head
s_head = snake_game.segments[0]


my_screen.listen()
my_screen.onkey(snake_game.up, "Up")
my_screen.onkey(snake_game.down, "Down")
my_screen.onkey(snake_game.right, "Right")
my_screen.onkey(snake_game.left, "Left")

is_running = True

while is_running:
    my_screen.update()
    time.sleep(0.3)
    snake_game.move()


    #Detect collision with food
    if snake_game.segments[0].distance(my_food) < 14:
        scoreboard.increment()
        snake_game.extend_snake()
        my_food.start_afresh()
    
    #Detect collision with tail
    for each_segment in snake_game.segments[1:]:
        if each_segment.distance(s_head) < 14:
            scoreboard.game_over()
            is_running = False
    
    #Game Over!!!
    if s_head.xcor() > 300 or s_head.ycor() > 300 or s_head.xcor() < -300 or s_head.ycor() < -300:
        scoreboard.game_over()
        is_running = False
    
       
        

    











my_screen.exitonclick()
