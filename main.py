from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("orange")
screen.title("PING POING GAME IN PYTHON")

paddle = Paddle()

paddle

screen.exitonclick()