import time
import turtle
import random
delay=0.2

# score
score = 0
high_score = 0

#set up the screen
wn=turtle.Screen()
wn.title("sname game ")
wn.bgcolor("blue")
wn.setup(width=600,height=600)
wn.tracer(0)


#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0  high score: 0", font=(15))

#functions

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_right():
    if head.direction != "left":
        head.direction="right"

def go_left():
    if head.direction != "right":
        head.direction="left"

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")



#main game loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(3)
        head.goto(0,0)
        head.direction=="stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list
        segments.clear()

        #reset the score
        score=0

        pen.clear()
        pen.write("score: {} high score: {}".format(score,high_score), font=(15))

    

    #check for a collision with food and food in a random spot
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #new segment of turtle
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #increase the score
        score +=10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score: {} high score: {}".format(score,high_score), font=(15))

    #move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
         

    #move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
         

    move()

    #check for body collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(3)
            head.goto(0,0)
            head.direction="stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segment list
            segments.clear()    

            #reset the score
            score=0

            pen.clear()
            pen.write("score: {} high score: {}".format(score,high_score), font=(15))

            


    time.sleep(delay)

wn.mainloop()
