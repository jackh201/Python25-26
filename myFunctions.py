import turtle
bob=turtle.Turtle()

#polygon
def polygon(sides, distance):
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

#circle
def circle(radius,border_color):
    bob.pencolor(border_color)
    bob.circle(radius)

#comet
def comet(distance,angle,color):
    bob.pencolor(color)
    for times in range(10):
        bob.width(times*0.5)
        bob.forward(distance)
        bob.left(angle)

#comet_right
def comet_right(distance,angle,color):
    bob.pencolor(color)
    for times in range(10):
        bob.width(times*0.5)
        bob.forward(distance)
        bob.right(angle)

#jump
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

#stair
def stair(distance,amount2):
     for times in range(amount2):
         bob.forward(distance)
         bob.left(90)
         bob.forward(distance)
         bob.right(90)

#spiral
def spiral(distance,amount1):
    for times in range(amount1):
        comet(distance,20)
        jump(0,0)
        bob.left(times+30)
 
# Tree Design 1  
def tree1(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50,)#square(trunk of tree)
  jump(-25 + x , 50 + y)
  bob.color("green")
  polygon(3, 100)#1st triangle(tree top)
  jump(-25 + x, 75 + y)
  polygon(3, 100)#2nd triangle(tree top)
  
# Tree Design 2
def tree2(x,y):
  jump(x,y)
  bob.pensize(5)
  bob.color("brown")
  polygon(4, 50)
  bob.color("green")
  jump(-10 + x, 50 + y)
  bob.circle(40)
  jump(60 + x, 50 + y)
  bob.circle(40)
  jump(25 + x, 75 + y)
  bob.circle(40)
  jump(25 + x, 25 + y)
  bob.circle(40)

# Sun design
def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)

# Triangle1
def triangle1(leg,color):
    bob.pencolor(color)
    bob.fillcolor(color)
    bob.begin_fill()
    bob.forward(leg)
    bob.left(30)
    bob.forward(leg)
    bob.left(165)
    bob.forward(leg*2)
    bob.end_fill()
    bob.setheading(0)
    
# Flower1
def flower1(x,y,size,c1,c2,c3,c4):
    jump(x,y)
    bob.pensize(0.1)
    for times in range(13):
        triangle1(size*4.5,c1)
        jump(x,y)
        bob.setheading(0)
        bob.left(30*times)
    jump(x,y)
    bob.setheading(0)
    bob.pencolor(c2)
    for times in range(25):
        comet(size/1.4,5,c2)
        jump(x,y)
        bob.setheading(0)
        bob.left(15*times)
    jump(x,y)
    bob.setheading(0)
    bob.pensize(5)
    for times in range(8):
        circle(size*2.5,c3)
        bob.left(45)
    jump(x,y)
    bob.setheading(0)
    bob.pensize(1)
    for times in range(16):
        circle(size,c4)
        bob.left(22.5)

#Flower2
def flower2(x,y,size,c1,c2):
    jump(x,y)
    bob.pensize(0.1)
    for times in range(13):
        triangle1(size*4.5,c1)
        jump(x,y)
        bob.setheading(0)
        bob.left(30*times)
    jump(x,y)
    bob.setheading(0)
    bob.pencolor(c2)
    for times in range(25):
        comet(size/1.4,5,c2)
        jump(x,y)
        bob.setheading(0)
        bob.left(15*times)

        
#turn
def turn(angle,distance):
    bob.left(angle)
    bob.forward(distance)







