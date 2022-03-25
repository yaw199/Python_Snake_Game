from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed(0)
        randx = random.randint(-270,270)
        randy = random.randint(-270,270)
        self.goto((randx,randy))

    def start_afresh (self):
        randx = random.randint(-270,270)
        randy = random.randint(-270,270)
        self.goto((randx,randy))
