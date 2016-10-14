from turtle import *   # it's ya boi
from os import system   # import only one function
from platform import system as platform   # import platform system as platform
from time import sleep   # import one func
from Tkinter import *   # need this too


class Letters(object):  # class inherits from Funcs

    def prepare(self, val):  # prepare the turtle
        sleep(0.5)  # wait
        turt.hideturtle()  # hide it
        turt.reset()  # reset it
        turt.clear()  # clear it
        turt.penup()  # lift the pen
        turt.color("green")  # change the color
        turt.setx(val)  # set the x
        turt.showturtle()  # show it
        turt.pendown()  # put the pen down

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
        self.prepare(0)
        t.right(180)
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
        t.forward(135)
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
        self.prepare(0)
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
        t.right(68)
        t.forward(141)
        t.left(135)
        t.forward(141)
        t.right(135)
        t.forward(141)
        t.left(135)
        t.forward(141)

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


class Funcs(Letters):  # new function class

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
        global turt  # global var
        turt = Turtle()  # now is a Turtle

    def destroy(self, value):
        root.destroy()  # destroys the window

    def draw_name(self, value):  # the main function
        self.window_front()  # window to front
        your_name = name_getter.get()  # get it
        your_name = your_name.lower()  # lower it
        for i in range(0, len(your_name)):  # for loop
            if your_name[i] == "a":  # if the name with index i = "a"
                self.A(turt)  # call the func
            elif your_name[i] == "b":
                self.B(turt)
            elif your_name[i] == "c":
                self.C(turt)
            elif your_name[i] == "d":
                self.D(turt)
            elif your_name[i] == "e":
                self.E(turt)
            elif your_name[i] == "f":
                self.F(turt)
            elif your_name[i] == "g":
                self.G(turt)
            elif your_name[i] == "h":
                self.H(turt)
            elif your_name[i] == "i":
                self.I(turt)
            elif your_name[i] == "j":
                self.J(turt)
            elif your_name[i] == "k":
                self.K(turt)
            elif your_name[i] == "l":
                self.L(turt)
            elif your_name[i] == "m":
                self.M(turt)
            elif your_name[i] == "n":
                self.N(turt)
            elif your_name[i] == "o":
                self.O(turt)
            elif your_name[i] == "p":
                self.P(turt)
            elif your_name[i] == "q":
                self.Q(turt)
            elif your_name[i] == "r":
                self.R(turt)
            elif your_name[i] == "s":
                self.S(turt)
            elif your_name[i] == "t":
                self.T(turt)
            elif your_name[i] == "u":
                self.U(turt)
            elif your_name[i] == "v":
                self.V(turt)
            elif your_name[i] == "w":
                self.W(turt)
            elif your_name[i] == "x":
                self.X(turt)
            elif your_name[i] == "y":
                self.Y(turt)
            elif your_name[i] == "z":
                self.Z(turt)
            turt.hideturtle()
