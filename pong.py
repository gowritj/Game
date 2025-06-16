import turtle as t
import winsound
wn=t.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A

paddle_a=t.Turtle()
paddle_a.speed(0)
paddle_a.color("purple")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B

paddle_b=t.Turtle()
paddle_b.speed(0)
paddle_b.color("purple")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball=t.Turtle()
ball.speed(5)
ball.color("yellow")
ball.shape("circle")
ball.penup()
ball.goto(0,0)

ball.dx=0.1
ball.dy=0.1

#score

score_a=0
score_b=0

#pen

pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A:0 player B:0",align="center",font=("courier",24,"normal"))

#Moving Paddles

def paddle_a_up():
    y=paddle_a.ycor()
    y+=30
    if y>=250:
        y=250   
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=30
    if y<=-250:
        y=-250 
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    if y>=250:
        y=250 
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    if y<=-250:
        y=-250 
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
          
    import random
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= random.choice([-1,1])
        score_a+=1
        pen.clear()
        pen.write("player A:{} player B:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= random.choice([-1,1])
        score_b+=1
        pen.clear()
        pen.write("player A:{} player B:{}".format(score_a,score_b),align="center",font=("courier",24,"normal"))
        winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
        
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50) and (ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50) and (ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
