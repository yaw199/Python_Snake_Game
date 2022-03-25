from turtle import Turtle

#Constant variable must be uppercase in Python
SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        #Create Snake bodies
        for each_post in SNAKE_POSITIONS:
            self.add_segment(each_post)
    
    def add_segment(self,each_position):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(each_position)
            self.segments.append(snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    
    def move(self):
        for back_num in range(len(self.segments)-1,0,-1):
            newx = self.segments[back_num-1].xcor()
            newy = self.segments[back_num-1].ycor()
            self.segments[back_num].goto(newx,newy)
        self.segments[0].forward(MOVE_DISTANCE)

    #Keyboard functions or methods
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
