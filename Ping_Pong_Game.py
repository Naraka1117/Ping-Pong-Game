import turtle

window = turtle.Screen() 

window.title("Ping Pong by Omar") 

window.bgcolor("black") 

window.setup(width = 800,height = 600) 

window.tracer(0) 


racket1 = turtle.Turtle()

racket1.speed(0)

racket1.shape("square")

racket1.color("blue")

racket1.shapesize(stretch_wid = 6 , stretch_len = 1)

racket1.penup()

racket1.goto(-350,0)



racket2 = turtle.Turtle()
   
racket2.speed(0)

racket2.shape("square")

racket2.color("red")

racket2.shapesize(stretch_wid = 6 , stretch_len = 1)

racket2.penup()

racket2.goto(350,0)



ball = turtle.Turtle()
   
ball.speed(0)

ball.shape("square")

ball.color("white")

ball.penup()

ball.goto(0,0)

ball.dx = 0.1

ball.dy = 0.1

score1 = 0

score2 = 0

score = turtle.Turtle()

score.speed(0)

score.color("white")

score.penup()

score.hideturtle()

score.goto(0,260)

score.write("Player 1 : 0 Player 2 : 0",align = "center" , font = ("Courier",24,"normal"))

def racket1_up():
    y = racket1.ycor()
    y += 20
    racket1.sety(y)
    

def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)
    

def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)


window.listen()
window.onkeypress(racket1_up,"w")
window.onkeypress(racket1_down,"s")

window.onkeypress(racket2_up,"Up")
window.onkeypress(racket2_down,"Down")


while True :
    
    window.update() #updates the screen 
    
    ball.setx(ball.xcor() + ball.dx)
    
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align = "center" , font = ("Courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align = "center" , font = ("Courier",24,"normal"))
        
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        