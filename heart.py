from turtle import *  # it's ya boi
from os import system  # import only one function
from platform import system as platform  # import platform system as platform


t = Turtle()
if platform() == "Darwin":  # how Mac OS X is identified by Python
    system("""/usr/bin/osascript -e 'tell app "Finder" to set
    frontmost of process "Python" to true' """)  # window to front


class IHeartU(object):
    """
    Makes an I <3 U.
    """

    def __init__(self):
        pass

    def i(self):
        t.speed(6)
        t.penup()
        t.color("red")
        t.setx(-300)
        t.sety(-100)
        t.pendown()
        t.fill(True)
        t.forward(30)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(75)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(75)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(15)
        t.fill(False)
        t.penup()
        t.right(90)
        t.forward(15)
        t.sety(-205)

    def heart(self):
        t.setx(0)
        t.color("red")
        t.pendown()
        t.fill(True)
        t.forward(10)
        for x in range(0, 5):
            t.left(90)
            t.forward(25)
            t.right(90)
            t.forward(25)
        t.left(90)
        t.forward(75)
        t.left(90)
        t.forward(145)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(145)
        t.left(90)
        t.forward(75)
        for x in range(0, 5):
            t.left(90)
            t.forward(25)
            t.right(90)
            t.forward(25)
        t.left(90)
        t.setx(10)
        t.fill(False)
        t.penup()

    def u(self):
        t.forward(260)
        t.pendown()
        t.fill(True)
        t.left(90)
        t.forward(105)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(90)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(90)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(105)
        t.left(90)
        t.forward(45)
        t.fill(False)
        t.hideturtle()


new_t = IHeartU()
new_t.i()
new_t.heart()
new_t.u()
t.getscreen()._root.mainloop()
