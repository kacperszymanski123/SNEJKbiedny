from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__('circle')
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.travel()

    def travel(self):
        self.goto((random.randint(-280, 280), random.randint(-280, 280)))
