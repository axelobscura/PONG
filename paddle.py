from turtle import Screen, Turtle

screen = Screen()

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)