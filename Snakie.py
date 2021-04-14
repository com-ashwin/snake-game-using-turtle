import turtle
import time
import random


delay=0.1
score=0
highestScore=0

#snake body
bodies=[]

#game screen
scr=turtle.Screen()
scr.bgcolor("gray")
scr.title("Snakie")
scr.setup(width=600,height=600)

#Snake head

head=turtle.Turtle()
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.speed(0)
head.penup()
head.goto(0,0)
#head.shapesize()
head.direction="stop"

#snake food

food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("yellow")
food.fillcolor("orange")
food.penup()
food.ht()
food.goto(0,10)
food.shapesize(1)
food.st()


#scoreboard
sb=turtle.Turtle()
#sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.goto(-250,-250)
sb.write("Score : 0   | Highest Score : 0")


def moveup():
    if head.direction!="down":
        head.direction="up"

def movedown():
    if head.direction!="up":
        head.direction="down"

def moveright():
    if head.direction!="left":
        head.direction="right"
        
def moveleft():
    if head.direction!="right":
        head.direction="left"

def moveStop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+10)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-10)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+10)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-10)

#event handlings

scr.listen()
scr.onkey(moveup,"Up")
scr.onkey(movedown,"Down")
scr.onkey(moveleft,"Left")
scr.onkey(moveright,"Right")


#snake entire logic

while True:
    scr.update() #update the screen

    #cross the window and come from oppsosite direction or collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.ycor()>290:
        head.sety(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()<-290:
        head.sety(290)

    #changing food position
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    
    #increasing size of body
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("yellow")
        body.fillcolor("red")
        bodies.append(body)

    #increase the score
        score+=10

    #change delay
        delay-=0.001

    #update highest score
        if score>highestScore:
          highestScore=score
        sb.clear()
        sb.write("Score : {} Highest score :{}".format(score,highestScore))



    #move snake body
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)

    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()


    #check collision with snake body
    for body in bodies:
        if body.distance(head)<10:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            sb.clear()
            sb.write("Score : {}  | Highest score :{}".format(score,highestScore))
    time.sleep(delay)
scr.mainloop()


        
        










turtle.Screen().exitonclick()



