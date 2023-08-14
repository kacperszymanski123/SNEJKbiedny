from turtle import Turtle
DISTance = 20

class Snake:
    def __init__(self):
        startowe = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for el in startowe:
            segment = Turtle('square')
            segment.color('white')
            segment.up()
            segment.goto(el)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[i - 1].xcor()
            newY = self.segments[i - 1].ycor()
            self.segments[i].goto((newX, newY))
        self.segments[0].forward(DISTance)

    def up(self):
        if self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90.0:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0)

