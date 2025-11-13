from myFunctions import*
turtle.colormode(255)
turtle.tracer(0)
from random import randint

turtle.bgcolor("black")
bob.speed(0)


#background
for times in range(5):
    jump(0,times*-50-50)
    bob.setheading(0)
    circle(times*50+50,"black")

jump(0,0)
bob.setheading(0)
bob.pensize(1)
bob.pencolor(255,0,0)
for times in range(120):
    bob.forward(times*10)
    bob.left(90)

jump(7,7)
bob.setheading(0)
bob.pensize(1)
bob.pencolor(0,255,0)
for times in range(120):
    bob.forward(times*10)
    bob.left(90)

jump(-7,-7)
bob.setheading(0)
bob.pensize(1)
bob.pencolor(0,0,255)
for times in range(120):
    bob.forward(times*10)
    bob.left(90)


#zero lap
jump(0,50)
bob.pensize(2)

for times in range(50):
    c0=(255-times*5,0,times*5)
    jump(0,-50+times)
    bob.setheading(0)
    circle(50-times,c0)


#outside comet
jump(0,0)
bob.setheading(0)
bob.pensize(1)
for times in range(10):
    bob.left(times*36+36)
    comet(60,15,"red")
    jump(0,0)
    bob.setheading(0)
    

jump(0,0)
bob.setheading(0)
for times in range(10):
    bob.left(times*36+24)
    comet(60,15,"green")
    jump(0,0)
    bob.setheading(0)
    
jump(0,0)
bob.setheading(0)
for times in range(10):
    bob.left(times*36+12)
    comet(60,15,"blue")
    jump(0,0)
    bob.setheading(0)
    

#first lap
jump(0,-100)
bob.setheading(0)
bob.pensize(5)

for times in range(40):
    circle(25,"red")
    turn(2.9,5.1365)
    circle(25,"blue")
    turn(3,5.1365)
    circle(25,"green")
    turn(3,5.1365)

    
#second lap
jump(0,-150)
bob.setheading(0)
bob.pensize(7)
c1=(255,0,0)
c2=(190,0,0)
c3=(130,0,0)
c4=(80,0,0)
c5=(30,0,0)

for times in range(25):
    circle(25,c1)
    turn(2.86,7.686)
    circle(25,c2)
    turn(3,7.686)
    circle(25,c3)
    turn(3,7.686)
    circle(25,c4)
    turn(3,7.686)
    circle(25,c5)
    turn(3,7.686)


#third lap   
jump(0,-200)
bob.setheading(0)
bob.pensize(9)
c5=(0,255,0)
c6=(0,190,0)
c7=(0,140,0)
c8=(0,80,0)
c9=(0,35,0)

for times in range(26):
    circle(25,c5)
    bob.left(2.86)
    bob.forward(10.27)
    circle(25,c6)
    bob.left(3)
    bob.forward(10.27)
    circle(25,c7)
    bob.left(3)
    bob.forward(10.27)
    circle(25,c8)
    bob.left(3)
    bob.forward(10.27)
    circle(25,c9)
    turn(3,10.27)


#fourth lap
jump(0,-250)
bob.setheading(0)
bob.pensize(12)
c9=(0,0,255)
c10=(0,0,200)
c11=(0,0,140)
c12=(0,0,90)
c13=(0,0,35)

for times in range(27):
    circle(25,c9)
    bob.left(2.86)
    bob.forward(12.82)
    circle(25,c10)
    turn(3,12.82)
    circle(25,c11)
    turn(3,12.82)
    circle(25,c12)
    turn(3,12.82)
    circle(25,c13)
    turn(3,12.82)


#fifth lap
jump(0,-300)
bob.setheading(0)
bob.pensize(15)
c1=(255,0,0)
c2=(190,0,0)
c3=(130,0,0)
c4=(80,0,0)
c5=(30,0,0)

for times in range(28):
    circle(25,c1)
    turn(2.86,15.37)
    circle(25,c2)
    turn(3,15.37)
    circle(25,c3)
    turn(3,15.37)
    circle(25,c4)
    turn(3,15.37)
    circle(25,c5)
    turn(3,15.37)


#inside comet
jump(-1,0)
bob.setheading(0)
for times in range(10):
    bob.left(times*36+36)
    comet(11,15,"green")
    jump(-1,0)
    bob.setheading(0)

jump(-1,0)
bob.setheading(0)
for times in range(10):
    bob.left(times*36+24)
    comet(11,15,"red")
    jump(-1,0)
    bob.setheading(0)

jump(-1,0)
bob.setheading(0)
for times in range(10):
    bob.left(times*36+12)
    comet(11,15,"blue")
    jump(-1,0)
    bob.setheading(0)


#center
jump(-1,0)
bob.setheading(0)
for times in range(12):
    comet(3,5,"red")
    jump(-1,0)
    bob.setheading(0)
    bob.left(times*30+30)
for times in range(12):
    comet_right(3,5,"blue")
    jump(-1,0)
    bob.setheading(0)
    bob.left(times*30+30)
