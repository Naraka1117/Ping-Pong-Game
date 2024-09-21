import turtle

window = turtle.Screen() 

window.title("Ping Pong by Omar") 

window.bgcolor("black") 

window.setup(width = 800,height = 600) 

window.tracer(0) 

#-----------------Left player-----------------#
racket1 = turtle.Turtle()

racket1.speed(0)

racket1.shape("square")

racket1.color("blue")

racket1.shapesize(stretch_wid = 6 , stretch_len = 1)

racket1.penup()

racket1.goto(-350,0)


#-----------------Right player-----------------#
racket2 = turtle.Turtle()
   
racket2.speed(0)

racket2.shape("square")

racket2.color("red")

racket2.shapesize(stretch_wid = 6 , stretch_len = 1)

racket2.penup()

racket2.goto(350,0)


#-----------------Ball-----------------#
ball = turtle.Turtle()
   
ball.speed(0)

ball.shape("square")

ball.color("white")

ball.shapesize(stretch_wid = 1 , stretch_len = 1)

ball.penup()

ball.goto(0,0)

ball.dx = 0.2 #Ball movement speed

ball.dy = 0.2 #Ball movement speed

#-----------------Score-----------------#
score1 = 0 #Left player score

score2 = 0 #Right player score

score = turtle.Turtle()

score.speed(0)

score.color("white")

score.penup()

score.hideturtle()

score.goto(0,260)

score.write("Player 1 : 0 Player 2 : 0",align = "center" , font = ("Courier",24,"normal"))


#-----------------Movment start-----------------#
def racket1_up(): #Left player
    y = racket1.ycor()
    y += 20
    racket1.sety(y)
    

def racket1_down(): #Left player
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)
    

def racket2_up(): #Right player
    y = racket2.ycor()
    y += 20
    racket2.sety(y)


def racket2_down(): #Right player
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)


#-----------------Keyboard binding-----------------#
window.listen()
#For the left player
window.onkeypress(racket1_up,"w")
window.onkeypress(racket1_down,"s")

#For the right player
window.onkeypress(racket2_up,"Up")
window.onkeypress(racket2_down,"Down")

#-----------------Main game loop-----------------#
while True :
    
    window.update() #updates the screen 
    
    ball.setx(ball.xcor() + ball.dx) #ball movement on x axis
    
    ball.sety(ball.ycor() + ball.dy) #ball movement on y axis
    
    #Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    #Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #Right goal
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align = "center" , font = ("Courier",24,"normal"))
        ball.dx = 0.2
        ball.dy = 0.2

    #Left goal
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align = "center" , font = ("Courier",24,"normal"))
        ball.dx = 0.2
        ball.dy = 0.2

    #Right racket and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 344) and (ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor() -40):
        ball.setx(330)
        ball.dx *= -1
        ball.dx += 0.05
        ball.dy += 0.05
    
    #Left racket and ball collisions
    if (ball.xcor() < -330 and ball.xcor() > -344) and (ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor() -40):
        ball.setx(-330)
        ball.dx *= -1
        ball.dx += 0.05
        ball.dy += 0.05 
        