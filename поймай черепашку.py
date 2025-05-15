import turtle
import random
import time

screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write("Score: 0", align="center", font=("Arial", 24, "normal"))

score = 0
game_time = 30
start_time = time.time()

def move_turtle():
    """Move the turtle to a random position."""
    x = random.randint(-280, 280)
    y = random.randint(-240, 240)
    player.goto(x, y)

def update_score():
    """Update the score display."""
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

def clicked(x, y):
    global score
    score += 1
    update_score()
    move_turtle()

def game_over():
    player.hideturtle()
    score_turtle.clear()
    score_turtle.goto(0, 0)
    score_turtle.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 30, "bold"))

player.onclick(clicked)

move_turtle()

while True:
    screen.update()
    elapsed = time.time() - start_time
    if elapsed > game_time:
        game_over()
        break

screen.mainloop()

