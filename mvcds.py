from Tkinter import *
from time import sleep
from os import system  # import only one function
from platform import system as platform  # import platform system as platform


class MVCDS(object):
    """
    To-do app.
    I'm aware there's an index error. Don't worry.
    """

    def __init__(self):
        self.my_bool_array = []
        self.my_stuff_array = []
        self.my_things_array = []
        self.root = Tk()
        self.root.wm_title("ToDo")
        self.done_button = Button(self.root,
            text="Done!", command=self._delete)
        self.done_button.pack()
        self.add_button = Button(self.root,
            text="Make it happen!", command=self._create)
        self.my_thing = Entry(self.root)
        self.my_thing.pack()
        self.add_button.pack()
        self.my_thing.focus_set()
        self.my_thing.bind("<Return>", self._create)  # bind the enter key
        self.my_thing.bind("<Escape>", self._destroy)  # bind the escape key
        self._front()
        self.root.mainloop()

    def _front(self):
        if platform() == "Darwin":  # how Mac OS X is identified by Python
            system("""/usr/bin/osascript -e 'tell app "Finder" to set \
            frontmost of process "Python" to true' """)  # window to front

    def _create(self, value=None):
        self.mine_to_check = BooleanVar(self.root)
        self.my_thing_to_add = self.my_thing.get()
        if self.my_thing_to_add in self.my_things_array:
            self.warn_window = Toplevel(self.root)
            self.warning = Entry(self.warn_window)
            self.warning.insert(0, "You already added that!")
            self.warning.pack()
        elif self.my_thing_to_add:
            self.my_things_array.append(self.my_thing_to_add)
            self.my_thing.delete(0, END)
            self.my_bool_array.append(self.mine_to_check)
            for x in range(0, len(self.my_bool_array)):
                self.my_stuff = Checkbutton(self.root,
                    text=self.my_thing_to_add, variable=self.my_bool_array[x])
            self.my_stuff_array.append(self.my_stuff)
            for x in range(0, len(self.my_stuff_array)):
                self.my_stuff_array[x].pack()
        else:
            self.warn_window = Toplevel(self.root)
            self.warning = Entry(self.warn_window)
            self.warning.insert(0, "You added nothing!")
            self.warning.pack()

    def _del(self, n):
        if self.my_bool_array[n].get():
            self.my_stuff_array[n].pack_forget()
            del self.my_bool_array[n]
            del self.my_stuff_array[n]
            del self.my_things_array[n]

    def _destroy(self, value=None):  # destroy method
        self.root.destroy()  # destroys the window

    def _delete(self):
        for x in range(0, len(self.my_stuff_array)):
            while (self.my_bool_array[x].get()):
                try:
                    self._del(x)
                except IndexError:
                    for i in range(0, len(self.my_bool_array)):
                        self._del(i)
                sleep(0.01)


my_app = MVCDS()
