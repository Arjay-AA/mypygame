import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off screen updates for performance

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target turtle
target = turtle.Turtle()
target.shape("square")
target.color("red")
target.penup()
target.speed(0)
target.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Score variable
score = 0

# Score display turtle
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Functions to move the player turtle
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    # Check for collision with the target
    if player.distance(target) < 20:
        # Move the target to a new random position
        target.setposition(random.randint(-290, 290), random.randint(-290, 290))
        # Increase the score
        score += 1
        # Update the score display
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    
    # Update the screen
    wn.update()