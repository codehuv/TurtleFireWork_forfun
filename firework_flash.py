#!/usr/bin/env python
# coding: utf-8

# In[22]:


import turtle
import random


# In[40]:


def init():
    turtle.reset()
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.speed(0)
    turtle.penup()
    turtle.left(90)
    turtle.goto(0,-450)
    turtle.speed(3)

def read_position():
    return turtle.xcor(), turtle.ycor()

def shoot():
    turtle.setheading(90)
    init_x,init_y = read_position()
#     #set clearner
#     clearner = turtle()
#     clearner.hideturtle()
#     clearner.speed(2)
#     clearner.goto(init_x, init_y)
#     clearner.pencolor('black')
    
    turtle.pendown()
    turtle.hideturtle()
    move = random.randint(280,580)
    
    #set random color
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    turtle.pencolor(r,g,b)
    
    #set speed
    turtle.speed(1)
    turtle.forward(move)
    
    #draw circle
    turtle.speed(0)
    spread = random.randint(50,100)
    for i in range(36):
        turtle.right(10)
        turtle.forward(spread)
        turtle.backward(spread)
        
    
    #done
    turtle.penup()
    turtle.colormode(1)
    turtle.pencolor('white')
    turtle.speed(0)
    turtle.goto(init_x,init_y)
    turtle.speed(3)
    turtle.showturtle()

def move_right():
    turtle.setheading(0)
    turtle.forward(10)

def move_left():
    turtle.setheading(180)
    turtle.forward(10)


# In[42]:


init()
turtle.listen()

turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right,"Right") 
turtle.onkeypress(shoot, 'Up')
turtle.onkeypress(init,'space')

turtle.mainloop()

