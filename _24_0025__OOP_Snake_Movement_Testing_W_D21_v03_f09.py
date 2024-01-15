from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Siris's Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments_list = []

# Initialize snake segments
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake_segments_list.append(new_segment)

def rotate_counter_clockwise():
    snake_segments_list[0].left(90)

def rotate_clockwise():
    snake_segments_list[0].right(90)

screen.listen()
screen.onkey(fun=rotate_counter_clockwise, key="Left")
screen.onkey(fun=rotate_clockwise, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)

    # Move the end segments first in reverse order
    for i in range(len(snake_segments_list) - 1, 0, -1):
        new_x = snake_segments_list[i - 1].xcor()
        new_y = snake_segments_list[i - 1].ycor()
        snake_segments_list[i].goto(new_x, new_y)

    # Move the head of the snake
    snake_segments_list[0].forward(20)

screen.exitonclick()
