from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("orange")
screen.title("PING POING GAME IN PYTHON")
screen.tracer(0)
screen.listen()

paddle = Paddle()

screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()