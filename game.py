import turtle
import time
dlay=0.01
win = turtle.Screen()
win.setup(600,600)
win.bgcolor("#033F84")
win.tracer(0)
win.title("Ping Pong Game $OM")
#pad1
pad_1=turtle.Turtle()
pad_1.penup()
pad_1.shape("square")
pad_1.shapesize(1,5)
pad_1.color("White")
pad_1.goto(0,-270)

#pad2
pad_2=turtle.Turtle()
pad_2.penup()
pad_2.shape("square")
pad_2.shapesize(1,5)
pad_2.color("White")
pad_2.goto(0,270)

#pads movemonet
win.listen()
#move pad1
def move_right_pad_1():
    pad_1.setx(pad_1.xcor()+20)
def move_left_pad_1():
    pad_1.setx(pad_1.xcor()-20)
win.onkeypress(move_left_pad_1,"a")
win.onkeypress(move_right_pad_1,"d")
#move pad2
def move_right_pad_2():
    pad_2.setx(pad_2.xcor()+20)
def move_left_pad_2():
    pad_2.setx(pad_2.xcor()-20)
win.onkeypress(move_left_pad_2,"Left")
win.onkeypress(move_right_pad_2,"Right")

#ball
ball=turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("White")
ball.goto(0,0)
ball.bx=1.5
ball.by=2.5

#coustomize and scoring

owner=turtle.Turtle()
owner.penup()
owner.shape("circle")
owner.hideturtle()
owner.color("White")
owner.goto(-270,260)
owner.write("Created By Omar",font=("arial",10,"bold"))

c=[-295,-250,-200,-150,-100,-50,0,50,100,150,200,250,290]
for i in c:
    center = turtle.Turtle()
    center.shape("square")
    center.color("white")
    center.penup()
    center.shapesize(0.1,0.9)
    center.goto(i,0)
s1=0
s2=0
#pad_1
play1=turtle.Turtle()
play1.penup()
play1.shape("circle")
play1.hideturtle()
play1.color("White")
play1.goto(-270,-140)
play1.write("0",font=("arial",50,"bold"))
#pad2
play2=turtle.Turtle()
play2.penup()
play2.shape("circle")
play2.hideturtle()
play2.color("White")
play2.goto(-270,60)
play2.write("0",font=("arial",50,"bold"))



while True:
    win.update()
    #ball movement
    ball.sety(ball.ycor()+ball.by)
    ball.setx(ball.xcor()+ball.bx)
    if ball.ycor()>280:
        ball.goto(0,0)
        ball.by*=-1
        s1+=1
        play1.clear()
        play1.write(f"{s1}",font=("arial",50,"bold"))
        
    elif ball.ycor()<-280:
        ball.goto(0,0)
        ball.by*=-1
        s2+=1
        play2.clear()
        play2.write(f"{s2}",font=("arial",50,"bold"))
    elif ball.xcor()>280:
        ball.setx(280)
        ball.bx*=-1
    elif ball.xcor()<-280:
        ball.setx(-280)
        ball.bx*=-1
    #touch ball in pad
    if ball.ycor()>265 and (ball.xcor()<pad_2.xcor()+50 and ball.xcor()>pad_2.xcor()-50):
        ball.sety(265)
        ball.by*=-1
    elif  ball.ycor()<-265 and (ball.xcor()<pad_1.xcor()+50 and ball.xcor()>pad_1.xcor()-50):
        ball.sety(-265)
        ball.by*=-1
    time.sleep(dlay)