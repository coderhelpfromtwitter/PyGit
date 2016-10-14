#!/usr/bin/python
from Tkinter import *  # import Tkinter, but don't use dot method
from os import system  # import only one function
from platform import system as platform  # import platform system as platform
from time import clock  # import one func


class Calc(object):  # doesn't inherit anything

    """
    My very first Python class.
    Created on 9/14/16.
    """

    root = Tk()  # new window
    result = Text(root)  # the result text
    equate = Entry()  # equation entry
    time_taken = Text(root)
    z = None

    def __init__(self):  # this does nothing
        pass

    def helpness(self):  # helps you
        self.new_window = Toplevel(self.root)
        helper = Text(self.new_window)
        helper.insert(INSERT, "\
        // is equal to square root.\n\
        ** is equal to x^y.\n\
        * is multiplication.\n\
        / is divide.\n\
        + is addition.\n\
        - is subtract.\n\
        ~ (or shift `) in front of any number makes it negative.\n")
        self.new_window.bind("<Escape>", self.destroy_new)
        self.new_window.wm_title("help")
        helper.pack()
        self.z = "You've entered the help menu"

    def destroy(self, value):  # destroy method
        self.root.destroy()  # destroys the window

    def destroy_new(self, value):  # destroys the new window
        self.new_window.destroy()  # of which is in the class

    def try_submit(self, value):  # tries to submit
        try:  # try this
            self.submit(value)  # submit call
        except BaseException:  # otherwise
            self.result.delete("1.0", END)
            self.result.insert(INSERT, "Internal Error")  # do this

    def window_front(self):
        if platform() == "Darwin":  # how Mac OS X is identified by Python
            system("""/usr/bin/osascript -e 'tell app "Finder" to set \
            frontmost of process "Python" to true' """)  # window to front

    def submit(self, value):  # calculate func
        t1 = clock()
        equation = self.equate.get()  # equation variable
        i = 0  # i equals 0
        for chars in equation:  # for loop
            if equation[i] == "+":  # if they put in a plus sign
                if equation[0] == "~":  # if x is meant to be negative
                    x = -(float(equation[1:i]))  # make x a negative number
                else:  # otherwise
                    x = float(equation[0:i])  # x is positive
                if equation[(i + 1)] == "~":  # if y is negative
                    y = -(float(equation[(i + 2):]))  # make it so
                else:  # otherwise
                    y = float(equation[(i + 1):])  # y is positive
                if y and x:  # if x and y exist
                    self.z = str(x + y)  # z is the answer
                else:  # otherwise
                    self.z = "Error"  # error
            elif equation[i:(i + 2)] == "//":
                if equation[0] == "~":
                    x = -(float(equation[1:i]))
                else:
                    x = float(equation[0:i])
                if equation[(i + 2)] == "~":
                    y = -(float(equation[(i + 3):]))
                else:
                    y = float(equation[(i + 2):])
                if y != 1:
                    self.z = str(x ** float(1 / y))
                else:
                    self.z = "Error"
            elif equation[i:(i + 2)] == "**":
                if equation[0] == "~":
                    x = -(float(equation[1:i]))
                else:
                    x = float(equation[0:i])
                if equation[(i + 2)] == "~":
                    y = -(float(equation[(i + 3):]))
                else:
                    y = float(equation[(i + 2):])
                if y and x:
                    self.z = str(x ** y)
                else:
                    self.z = "Error"
            elif equation[i] == "*":
                if equation[0] == "~":
                    x = -(float(equation[1:i]))
                else:
                    x = float(equation[0:i])
                if equation[(i + 1)] == "~":
                    y = -(float(equation[(i + 2):]))
                else:
                    y = float(equation[(i + 1):])
                if y and x:
                    self.z = str(x * y)
                else:
                    self.z = "Error"
            elif equation[i] == "-":
                if equation[0] == "~":
                    x = -(float(equation[1:i]))
                else:
                    x = float(equation[0:i])
                if equation[(i + 1)] == "~":
                    y = -(float(equation[(i + 2):]))
                else:
                    y = float(equation[(i + 1):])
                if y and x:
                    self.z = str(x - y)
                else:
                    self.z = "Error"
            elif equation[i] == "/":
                if equation[0] == "~":
                    x = -(float(equation[1:i]))
                else:
                    x = float(equation[0:i])
                if equation[(i + 1)] == "~":
                    y = -(float(equation[(i + 2):]))
                else:
                    y = float(equation[(i + 1):])
                if y and x:
                    self.z = str(x / y)
                else:
                    self.z = "Error"
            elif equation == "h":
                self.helpness()
            else:
                self.z = "Error"
                i += 1
        self.result.delete("1.0", END)
        self.result.insert(INSERT, self.z)
        t2 = clock()
        t3 = str(t2 - t1) + " seconds to compute: " + \
            equation + ";"
        self.time_taken.delete("1.0", END)
        self.time_taken.insert(END, t3)

    def end_result(self):
        self.root.wm_title("calc.py")  # title is "calc.py"
        self.equate.bind("<Return>", self.try_submit)  # bind the enter key
        self.equate.bind("<Escape>", self.destroy)  # bind the escape key
        self.equate.pack()  # pack it
        self.equate.focus_set()  # focus the equation input
        self.result.pack()  # pack, pack, pack it up, pack it up, up
        self.time_taken.pack()  # packed
        self.window_front()  # make the window go to the front
        self.root.mainloop()  # mainloop for Tk

my_personal = Calc()  # new instance
my_personal.end_result()  # actual app
