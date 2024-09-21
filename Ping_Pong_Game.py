import turtle
import random

# Set up the screen
window = turtle.Screen()
window.title("Ping Pong by Omar")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# -----------------Left player-----------------#
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("blue")
racket1.shapesize(stretch_wid=6, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# -----------------Right player-----------------#
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=6, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# -----------------Ball-----------------#
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

# Ball starts with a random direction
ball.dx = random.choice([0.2, -0.2])  # Randomly start moving left or right
ball.dy = random.choice([0.2, -0.2])  # Randomly start moving up or down

# -----------------Score-----------------#
score1 = 0  # Left player score
score2 = 0  # Right player score

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1 : 0 Player 2 : 0", align="center", font=("Courier", 24, "normal"))

# -----------------Movment start-----------------#
def racket1_up():  # Left player
    y = racket1.ycor()
    if y < 250:  # Limit to top of screen
        y += 20
        racket1.sety(y)

def racket1_down():  # Left player
    y = racket1.ycor()
    if y > -250:  # Limit to bottom of screen
        y -= 20
        racket1.sety(y)

def racket2_up():  # Right player
    y = racket2.ycor()
    if y < 250:  # Limit to top of screen
        y += 20
        racket2.sety(y)

def racket2_down():  # Right player
    y = racket2.ycor()
    if y > -250:  # Limit to bottom of screen
        y -= 20
        racket2.sety(y)

# -----------------Keyboard binding-----------------#
window.listen()
# For the left player
window.onkeypress(racket1_up, "w")
window.onkeypress(racket1_down, "s")

# For the right player
window.onkeypress(racket2_up, "Up")
window.onkeypress(racket2_down, "Down")

# -----------------Main game loop-----------------#
while True:
    window.update()  # updates the screen

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)  # ball movement on x-axis
    ball.sety(ball.ycor() + ball.dy)  # ball movement on y-axis

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right goal
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = random.choice([0.2, -0.2])  # Random reset direction
        ball.dy = random.choice([0.2, -0.2])
        score1 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Left goal
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = random.choice([0.2, -0.2])  # Random reset direction
        ball.dy = random.choice([0.2, -0.2])
        score2 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Right racket and ball collisions
    if (330 < ball.xcor() < 344) and (racket2.ycor() - 40 < ball.ycor() < racket2.ycor() + 40):
        ball.setx(330)
        ball.dx *= -1
        if abs(ball.dx) < 1.5:  # Limit max speed
            ball.dx += 0.05
            ball.dy += 0.05

    # Left racket and ball collisions
    if (-344 < ball.xcor() < -330) and (racket1.ycor() - 40 < ball.ycor() < racket1.ycor() + 40):
        ball.setx(-330)
        ball.dx *= -1
        if abs(ball.dx) < 1.5:  # Limit max speed
            ball.dx += 0.05
            ball.dy += 0.05

    # Check if either player has won
    if score1 == 10 or score2 == 10:
        score.clear()
        winner = "Player 1" if score1 == 10 else "Player 2"
        score.write("{} wins!".format(winner), align="center", font=("Courier", 24, "normal"))
        break  # Exit the game loop
