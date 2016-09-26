from turtle import *   # it's ya boi
from os import system   # import only one function
from platform import system as platform   # import platform system as platform
from time import sleep   # import one func
from Tkinter import *   # need this too


class Funcs:  # new function class

    def __init__(self):  # this does nothing
        pass   # told you

    def start(self):  # new turtle func
        global root  # global root
        root = Tk()  # new Tk window
        global name_getter  # name_getter is now global
        name_getter = Entry()  # and is an entry
        name_getter.pack()  # pack it
        name_getter.bind("<Return>", self.draw_name)  # bind the enter key
        name_getter.bind("<Escape>", self.destroy)  # bind the escape key
        self.window_front()  # bring window to front
        name_getter.focus_set()  # bring focus to Entry
        self.new_turt()
        root.mainloop()  # main loop

    def window_front(self):
        if platform() == "Darwin":   # how Mac OS X is identified by Python
            system("""/usr/bin/osascript -e 'tell app "Finder" to set \
            frontmost of process "Python" to true' """)   # window to front

    def new_turt(self):
        global t  # global var
        t = Turtle()  # now is a Turtle

    def destroy(self, value):
        root.destroy()  # destroys the window

    def draw_name(self, value):  # the main function
        self.window_front()  # window to front
        i = 0  # i equals 0
        your_name = name_getter.get()  # get it
        your_name = your_name.lower()  # lower it
        for chars in your_name:  # for loop
            if your_name[i] == "a":  # if the name with index i = "a"
                self.A(t)  # call the func
            elif your_name[i] == "b":
                self.B(t)
            elif your_name[i] == "c":
                self.C(t)
            elif your_name[i] == "d":
                self.D(t)
            elif your_name[i] == "e":
                self.E(t)
            elif your_name[i] == "f":
                self.F(t)
            elif your_name[i] == "g":
                self.G(t)
            elif your_name[i] == "h":
                self.H(t)
            elif your_name[i] == "i":
                self.I(t)
            elif your_name[i] == "j":
                self.J(t)
            elif your_name[i] == "k":
                self.K(t)
            elif your_name[i] == "l":
                self.L(t)
            elif your_name[i] == "m":
                self.M(t)
            elif your_name[i] == "n":
                self.N(t)
            elif your_name[i] == "o":
                self.O(t)
            elif your_name[i] == "p":
                self.P(t)
            elif your_name[i] == "q":
                self.Q(t)
            elif your_name[i] == "r":
                self.R(t)
            elif your_name[i] == "s":
                self.S(t)
            elif your_name[i] == "t":
                self.T(t)
            elif your_name[i] == "u":
                self.U(t)
            elif your_name[i] == "v":
                self.V(t)
            elif your_name[i] == "w":
                self.W(t)
            elif your_name[i] == "x":
                self.X(t)
            elif your_name[i] == "y":
                self.Y(t)
            elif your_name[i] == "z":
                self.Z(t)
            i += 1  # add to i
        sleep(1)  # wait for 1 second

    def prepare(self, val):  # prepare the turtle
        sleep(0.5)  # wait
        t.hideturtle()  # hide it
        t.reset()  # reset it
        t.clear()  # clear it
        t.penup()  # lift the pen
        t.color("green")  # change the color
        t.setx(val)  # set the x
        t.showturtle()  # show it
        t.pendown()  # put the pen down


class Letters(Funcs):  # class inherits from Funcs

    def A(self, t):
        self.prepare(-50)
        t.left(60)
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.right(180)
        t.forward(50)
        t.left(60)
        t.forward(50)

    def B(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(50)

    def C(self, t):
        self.prepare(0)
        t.left(180)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)

    def D(self, t):
        self.prepare(-50)
        t.forward(40)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(100)

    def E(self, t):
        self.prepare(-50)
        t.forward(50)
        t.left(180)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(180)
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)

    def F(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(180)
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)

    def G(self, t):
        self.prepare(-50)
        t.forward(50)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(30)
        t.left(180)
        t.forward(60)
        t.left(180)
        t.forward(30)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(10)

    def H(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.left(180)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(180)
        t.forward(100)

    def I(self, t):
        self.prepare(-50)
        t.forward(50)
        t.left(180)
        t.forward(25)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(25)
        t.left(180)
        t.forward(50)

    def J(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(25)
        t.left(180)
        t.forward(25)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)

    def K(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.left(180)
        t.forward(50)
        t.left(135)
        t.forward(75)
        t.right(180)
        t.forward(75)
        t.left(90)
        t.forward(75)

    def L(self, t):
        self.prepare(-50)
        t.forward(50)
        t.left(180)
        t.forward(50)
        t.right(90)
        t.forward(100)

    def M(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.right(135)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(135)
        t.forward(100)

    def N(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.right(135)
        t.forward(125)
        t.left(135)
        t.forward(100)

    def O(self, t):
        self.prepare(-50)
        t.left(180)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(15)
        t.right(90)
        t.forward(60)
        t.right(90)
        t.forward(15)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(15)
        t.right(90)
        t.forward(60)
        t.right(90)
        t.forward(15)
        t.left(90)
        t.forward(20)

    def P(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(50)

    def Q(self, t):
        self.prepare(0)
        t.right(180)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(135)
        t.forward(25)
        t.right(180)
        t.forward(50)

    def R(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(135)
        t.forward(75)

    def S(self, t):
        self.prepare(-25)
        t.forward(25)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(25)

    def T(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(25)
        t.left(180)
        t.forward(50)

    def U(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(100)
        t.left(180)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)

    def V(self, t):
        self.prepare(-100)
        t.penup()
        t.sety(100)
        t.pendown()
        t.right(60)
        t.forward(125)
        t.left(120)
        t.forward(125)

    def W(self, t):
        self.prepare(-100)
        t.penup()
        t.sety(100)
        t.pendown()
        t.right(60)
        t.forward(125)
        t.left(120)
        t.forward(125)
        t.right(120)
        t.forward(125)
        t.left(120)
        t.forward(125)

    def X(self, t):
        self.prepare(-50)
        t.left(45)
        t.forward(100)
        t.left(180)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(180)
        t.forward(100)

    def Y(self, t):
        self.prepare(-50)
        t.left(90)
        t.forward(80)
        t.left(45)
        t.forward(40)
        t.left(180)
        t.forward(40)
        t.left(90)
        t.forward(40)

    def Z(self, t):
        self.prepare(0)
        t.left(180)
        t.forward(75)
        t.right(135)
        t.forward(100)
        t.left(135)
        t.forward(75)
