#!/usr/bin/python
from Project.logit import print_to_log  # local file
from os import system, path  # import two functions
from platform import system as platform   # import platform system as platform
from subprocess import Popen, PIPE  # needed for built-in terminal
from Tkinter import *   # need this too


class Main(object):
    """
    My own compiler.
    """

    def __init__(self):
        """
        Does nothing.
        """
        pass

    def create_file(self, value=None):
        """
        Creates a file then opens it.
        """
        if not path.isdir("Project"):
            system("mkdir Project")
        string_to_systemize = "echo \"#!/usr/bin/python\n" + \
            "# Please use fp = open(\'Project/yourfile.*\') " + \
            "when opening YOUR files\n" + \
            "# to not lose YOUR file in the jumble of OTHER files.\n" + \
            "# Also, do NOT delete the very first comment line.\n" + \
            "# \'logs.txt\' is your friend for your error logs.\"" + \
            "> Project/myfile.py"
        system(string_to_systemize)
        system("chmod +x Project/myfile.py")
        self.open_file()

    def save_file(self, value=None):
        """
        Saves a file.
        """
        text_to_save = str(self.my_text.get("1.0", END))
        fp = open("Project/myfile.py", "w")
        fp.write(text_to_save)
        fp.close()

    def open_file(self, value=None):
        """
        Opens the file.
        """
        fp = open("Project/myfile.py")
        file_contents = fp.read()
        self.my_text.delete("1.0", END)
        self.my_text.insert("1.0", file_contents)
        fp.close()

    def run_file(self, value=None):
        """
        Runs the file and outputs it to the text window.
        """
        self.save_file()
        self.p = Popen("./Project/myfile.py", stdout=PIPE, stderr=PIPE)
        output, errors = self.p.communicate()
        self.my_output.delete("1.0", END)
        self.my_output.insert("1.0", output)
        if errors != "":
            print_to_log(errors)
            self.my_output.configure(fg="red")
        else:
            self.my_output.configure(fg="white")
        self.my_output.insert("1.0", errors)

    def select_all(self, value=None):
        """
        Selects the whole text.
        """
        self.my_text.tag_add(SEL, "1.0", END)
        self.my_text.mark_set(INSERT, "1.0")
        self.my_text.see(INSERT)
        return "break"

    def copy_text(self, value=None):
        """
        Copies text.
        """
        self.my_text.event_generate("<<Copy>>")

    def paste_text(self, value=None):
        """
        Pastes text.
        """
        self.my_text.event_generate("<<Paste>>")
        self.current_area()

    def cut_text(self, value=None):
        """
        Cuts text.
        """
        self.my_text.event_generate("<<Cut>>")
        self.current_area()

    def insert_tab(self, value=None):
        """
        Inserts a tab, or 4 spaces.
        """
        self.my_text.insert(INSERT, " " * 3)

    def current_area(self, value=None):
        """
        Gets the current area of the cursor and outputs it.
        """
        my_area = self.my_text.index(INSERT)
        str(my_area)
        for x in range(0, len(my_area)):
            if my_area[x] == ".":
                my_y = my_area[0:x]
                my_x = my_area[x + 1:]
        my_new_area = "Ln: " + my_y + " | Col: " + my_x
        self.my_location.config(text=my_new_area)

    def quit_window(self, value=None):
        """
        Quits a Tk window.
        """
        exit()

    def passer(self, value=None):
        """
        Literally is just a pass function.
        """
        pass

    def go_to_line(self, value=None):
        """
        Goes to a line.
        """
        self.searcher = Toplevel()
        self.searcher.wm_title("Go To Line")
        self.line_number = Entry(self.searcher)
        on_clicker = Button(self.searcher, command=self.go_to, text="Go")
        self.line_number.pack()
        on_clicker.pack()

    def go_to(self, value=None):
        """
        Goes to a specific line.
        """
        self.go_to_this_line = self.line_number.get()
        self.my_text.mark_set(INSERT, str(float(self.go_to_this_line)))
        self.current_area()
        self.my_text.see(INSERT)
        self.searcher.destroy()

    def undo(self, value=None):
        """
        Undoes something.
        """
        self.my_text.event_generate("<<Undo>>")
        self.current_area()

    def redo(self, value=None):
        """
        Redoes something.
        """
        self.my_text.event_generate("<<Redo>>")
        self.current_area()

    def clear_edit(self, value=None):
        """
        Clears the edit clipboard.
        """
        self.my_text.edit_reset()

    def window_front(self):
        """
        Sets window to front.
        """
        if platform() == "Darwin":
            system("""/usr/bin/osascript -e 'tell app "Finder" to set \
            frontmost of process "Python" to true' """)

    def start(self):
        """
        Starts the compiler.
        """
        root = Tk()
        menubar = Menu(root)
        self.my_text = Text(root,
                            bg="gray9", insertbackground="white",
                            fg="white", wrap="word", undo=True,
                            tabs="1c", height="20", width="80")
        self.my_output = Text(root,
                              bg="gray9", insertbackground="white",
                              fg="white", height="10", width="80")
        self.my_location = Label(root,
                                 bg="gray9", fg="white", justify="right",
                                 text="Ln: 1 | Col: 0")
        self.my_text.pack()
        self.my_output.pack()
        self.my_location.pack(side=RIGHT)
        self.my_text.bind("<Command-s>", self.save_file)
        self.my_text.bind("<Command-o>", self.open_file)
        self.my_text.bind("<Command-r>", self.run_file)
        self.my_text.bind("<Command-n>", self.create_file)
        self.my_text.bind("<Command-a>", self.select_all)
        self.my_text.bind("<Tab>", self.insert_tab)
        self.my_text.bind("<KeyRelease>", self.current_area)
        self.my_text.bind("<ButtonRelease-1>", self.current_area)
        self.my_text.bind("<Command-q>", self.quit_window)
        self.my_text.bind("<Command-Control-l>", self.clear_edit)
        self.my_text.event_add("<<Paste>>", "<Command-v>")
        self.my_text.event_add("<<Copy>>", "<Command-c>")
        self.my_text.event_add("<<Cut>>", "<Command-x>")
        self.my_text.focus_set()
        filemenu = Menu(menubar, tearoff=0)
        editmenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.create_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Run", command=self.run_file)
        filemenu.add_command(label="Quit", command=self.quit_window)
        editmenu.add_command(label="Select All", command=self.select_all)
        editmenu.add_command(label="Undo", command=self.undo)
        editmenu.add_command(label="Redo", command=self.redo)
        editmenu.add_command(label="Copy", command=self.copy_text)
        editmenu.add_command(label="Paste", command=self.paste_text)
        editmenu.add_command(label="Cut", command=self.cut_text)
        editmenu.add_command(label="Go To Line", command=self.go_to_line)
        menubar.add_cascade(label="Files", menu=filemenu)
        menubar.add_cascade(label="EditText", menu=editmenu)
        root.config(menu=menubar)
        root.wm_title("Mere")
        self.window_front()
        root.mainloop()


my_compiler = Main()  # TODO: Make more features
my_compiler.start()
