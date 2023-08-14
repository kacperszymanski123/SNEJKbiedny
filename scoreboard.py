from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0,y=260)
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.write(f'Score: {self.score}', font=('Comic Sans MS', 16, 'normal'), align='center')

    def point(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=('Comic Sans MS', 16, 'normal'), align='center')

    def gameover(self):
        self.goto(0,0)
        self.write('Game over', font=('Comic Sans MS', 28, 'normal'), align='center')


