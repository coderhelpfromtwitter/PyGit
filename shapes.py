from __future__ import division  # required for create_new
from turtle import *  # it's ya boi
from os import system  # import only one function
from platform import system as platform  # import platform system as platform
from Tkinter import *  # barely need this


class Shapes:

    def __init__(self):
        pass

    def demon(self):
        t.speed(0)
        for x in range(0, 180):
            t.forward(x)
            t.left(x)

    def heart(self):
        t.color("red")
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

    def square(self):
        t.penup()
        t.setx(-50)
        t.sety(-50)
        t.pendown()
        for x in ["red", "yellow", "green", "blue"]:
            t.color(x)
            t.forward(100)
            t.left(90)

    def oval(self):
        for i in range(0, 10):
            t.forward(5)
            t.left(1)
        for x in range(10, 170):
            t.forward(1)
            t.left(1)
        for n in range(170, 180):
            t.forward(5)
            t.left(1)
        for i in range(180, 190):
            t.forward(5)
            t.left(1)
        for x in range(190, 350):
            t.forward(1)
            t.left(1)
        for n in range(350, 360):
            t.forward(5)
            t.left(1)

    def figure8(self):
        t.right(45)
        t.forward(50)
        for x in range(0, 275):
            t.forward(1)
            t.left(1)
        t.forward(105)
        for i in range(0, 275):
            t.forward(1)
            t.right(1)
        t.forward(50)

    def trapezoid(self):
        t.setx(-50)
        t.forward(100)
        t.left(110)
        t.forward(110)
        t.left(70)
        t.forward(70)
        t.left(70)
        t.forward(110)
        t.left(110)
        t.forward(100)

    def create_new(self, xyz):
        print(str(xyz) + "agon")
        t.speed(0)
        for number in range(0, xyz):
            t.forward(float(360 / xyz))
            t.left(float(360 / xyz))

    def smiley(self):
        t.penup()
        t.setx(-50)
        t.sety(50)
        t.pendown()
        for x in range(0, 4):
            t.forward(5)
            t.left(90)
        t.penup()
        t.sety(35)
        t.setx(-75)
        t.pendown()
        t.right(90)
        for x in range(0, 180):
            t.forward(2)
            t.left(1)
        t.penup()
        t.setx(100)
        t.sety(50)
        t.pendown()
        for x in range(0, 4):
            t.forward(5)
            t.left(90)


class Funcs(Shapes):

    def new_turt(self):
        global t  # global var
        t = Turtle()  # now is a Turtle

    def window_front(self):
        if platform() == "Darwin":   # how Mac OS X is identified by Python
            system("""/usr/bin/osascript -e 'tell app "Finder" to set \
            frontmost of process "Python" to true' """)  # window to front

    def destroy(self, value):
        root.destroy()  # destroys the window

    def start(self):  # new turtle func
        global root  # global root
        root = Tk()  # new Tk window
        global shape_getter  # shape_getter is now global
        shape_getter = Entry()  # and is an entry
        shape_getter.pack()  # pack it
        shape_getter.bind("<Return>", self.draw_shape)  # bind the enter key
        shape_getter.bind("<Escape>", self.destroy)  # bind the escape key
        self.window_front()  # bring window to front
        shape_getter.focus_set()  # bring focus to Entry
        self.new_turt()  # new turtle
        root.mainloop()  # main loop

    def draw_shape(self, value):
        new_shape = shape_getter.get()
        new_shape = new_shape.lower()
        t.reset()
        if new_shape == "demon":
            self.demon()
        elif new_shape == "heart":
            self.heart()
        elif new_shape == "square":
            self.square()
        elif new_shape == "oval":
            self.oval()
        elif new_shape == "figure 8":
            self.figure8()
        elif new_shape == "trapezoid":
            self.trapezoid()
        elif new_shape[0:6] == "create":
            try:
                number_of_sides = int(new_shape[7:])
                self.create_new(number_of_sides)
            except:
                print("Error")
        elif new_shape == "smiley":
            self.smiley()
        else:
            print("Error")
        t.hideturtle()
