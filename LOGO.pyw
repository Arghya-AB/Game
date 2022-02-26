import turtle,time
turtle.title("LOGO REVEAL!!! SHOWDOWN")
turtle.penup()
turtle.sety(170)
turtle.color('green')
style = ('Algerian', 30, 'italic')
turtle.write('WELCOME TO SHOWDOWN GAMES', font=style, align='center')
turtle.home()
turtle.pendown()

# What comes after the # is not seen by python. These are comments. :)

from turtle import * # imports the module turtle,
                    #* stands for all, which makes things easier

speed(0) # sets the speed of drawing to 0, which is the fastest
pencolor('yellow') # sets the color of the pen/lines to white
bgcolor('black') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0
up() # lifts up the pen, so no lines are drawn

#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle

rt(45) 
fd(90) 
rt(135) 

down() # sets down the pen, so that turtle can draw
while x < 120: # while the value of x is lesser than 120,
                #continuously do this:
    fd(75)     
    rt(61)
    fd(75)
    rt(61)
    fd(75)
    rt(61)
    fd(75)
    rt(61)
    fd(75)
    rt(61)
    fd(75)
    rt(61)

    rt(11.1111) 
    x = x+1 # adds 1 to the value of x,
            # so that it is closer to 120 after every loop
 # When you click, turtle exits.

#That's all! Try customizing the script! 8)
time.sleep(1)

turtle.bye()
