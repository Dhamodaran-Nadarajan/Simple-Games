# Simple Snake Game ©Dhamodaran Nadarajan

# Import Statements
import turtle
import time
import random

# Global Declarations - Start
width = 600
height = 600
delay = 0.1
score = 0
high_score = 0
left_border = int(-width / 2) + 10
down_border = int(-height / 2) + 10
right_border = int(width / 2) - 10
top_border = int(height / 2) - 10
coordinates = []
segments = []
for num in range(int(-width / 2) + 20, int(width / 2) - 19, 20):
    coordinates.append(num)

# Setting up the Window
window = turtle.Screen()
window.title("Snake_Game ©Dhamodaran Nadarajan")
window.bgcolor("black")
window.setup(width=width, height=height)
window.tracer(0)

# Setting up the Snake Head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.goto(0, 0)
snake_head.penup()
snake_head.direction = ""

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.choice(coordinates), random.choice(coordinates))

# Score_Board
score_board = turtle.Turtle()
score_board.color("white")
score_board.shape("square")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 270)
score_board.write("Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal"))


# After Collision Clear Snake Body segments, Reset food and Snake_Head
def clear_default():
    for segment in segments:
        segment.goto(1000, 10000)
    segments.clear()
    food.goto(random.choice(coordinates), random.choice(coordinates))


# Direction Control Functions
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


# Move Function
def move_snake():
    if snake_head.direction == "up":
        y_cord = snake_head.ycor()
        snake_head.sety(y_cord + 20)

    if snake_head.direction == "down":
        y_cord = snake_head.ycor()
        snake_head.sety(y_cord - 20)

    if snake_head.direction == "right":
        x_cord = snake_head.xcor()
        snake_head.setx(x_cord + 20)

    if snake_head.direction == "left":
        x_cord = snake_head.xcor()
        snake_head.setx(x_cord - 20)


# Input Listeners
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

# Main Game loop
while True:
    window.update()

    # Complexity Modifiers.
    if score > 5:
        delay = 0.07

    if score > 10:
        delay = 0.05

    # Border Collisions.
    if snake_head.xcor() > right_border or snake_head.xcor() < left_border or snake_head.ycor() > top_border or snake_head.ycor() < down_border:
        time.sleep(2)
        score = 0
        delay = 0.1
        score_board.clear()
        score_board.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 20, "normal"))
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        clear_default()

    # WHen snake_head eats food - Increases Snake Body by one segment and Reset Snake_Food.
    if snake_head.distance(food) < 20:
        # Reset Snake_Food location
        food.goto(random.choice(coordinates), random.choice(coordinates))

        # Create a body segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score count
        score += 1
        if score > high_score:
            # If current score is greater than high score - set new high score
            high_score = score

        # Display current score and high score
        score_board.clear()
        score_board.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 20, "normal"))

    # Move the snake body from tail to head.
    for index in range(len(segments) - 1, 0, -1):
        prev_segment_x_cord = segments[index - 1].xcor()
        prev_segment_y_cord = segments[index - 1].ycor()
        segments[index].goto(prev_segment_x_cord, prev_segment_y_cord)

    # Moves the first segment to the snake_head location.
    if len(segments) > 0:
        snake_head_x_cord = snake_head.xcor()
        snake_head_y_cord = snake_head.ycor()
        segments[0].goto(snake_head_x_cord, snake_head_y_cord)

    # Moves the snake head based on the direction assigned.
    move_snake()

    # Head collision with body segments
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(2)
            score = 0
            delay = 0.1
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            clear_default()

    # Controls the speed of the snake movement animation.
    time.sleep(delay)

wn.mainloop()
