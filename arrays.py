class FunWithLists(object):
    """
    This is my list of stuff I can do with lists.
    """

    def __init__(self, the_list):
        """
        This keeps code DRY.
        """
        self.tl = the_list

    def clear_list(self):
        """
        Basically deletes the entire list.
        """
        self.tl[:] = []

    def index_in_list(self, word_to_search):
        """
        Returns the index the word has in the list.
        """
        for elems in range(0, self.length_of_list()):
            if self.tl[elems] == word_to_search:
                return elems

    def count_in_list(self, word_to_search):
        """
        Returns how many times the word was found.
        """
        _count = 0
        for elem_to_search in self.tl:
            if elem_to_search == word_to_search:
                _count += 1
        return _count

    def depth(self, tl):
        """
        Returns the depth of a list.
        Cannot be created without a second parameter.
        """
        if self.length_of_list() > 0 and \
                isinstance(tl, list):
            return 1 + max(self.depth(item) for item in tl)
        else:
            return 0

    def reverse_list(self):
        """
        Reverses a list.
        """
        self.tl[::-1] = self.tl  # start:stop:step=-1

    def length_of_list(self):
        """
        Returns the amount of elements in a list.
        """
        length = 0
        for elems in self.tl:
            length += 1
        return length

    def sort_list(self):
        """
        Turns tl into a sorted one.
        """
        new_list = []  # brand new list
        while self.tl:  # while it exists
            minimum = self.tl[0]
            for elems in self.tl:
                if elems < minimum:
                    minimum = elems
            new_list[len(new_list):] = [minimum]
            self.tl.remove(minimum)  # no replacing this one
        for elems in new_list:
            self.tl[len(new_list):] = [elems]

    def flatten_2d(self):
        """
        Flattens a 2d list ONLY.
        """
        my_new_one = []
        i = 0
        for first_d in self.tl:
            if type(first_d) is not str and \
                        type(first_d) is not int and \
                        type(first_d) is not float:
                for second_d in first_d:
                    my_new_one[len(my_new_one):] = [second_d]
            else:
                my_new_one[len(my_new_one):] = [first_d]
        for more in my_new_one:
            try:
                self.tl[i] = more
            except IndexError:
                self.tl[self.length_of_list():] = [more]
            i += 1

    def flatten_it(self):
        """
        Flattens a list for the amount of depth it has.
        """
        for number in range(0, self.depth(self.tl)):
            self.flatten_2d()

    def pop_from_list(self):
        """
        Deletes and returns the last element of a list.
        """
        popper = self.tl[self.length_of_list() - 1]
        del self.tl[self.length_of_list() - 1]
        return popper

# below is an example N-dimensional list

my_list = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        ["John", "Deer"],
        ["I",
         ["am",
          ["in",
           ["a",
            ["list",
             ["Jane", "Doe"]
             ]
            ]
           ]
          ]
         ]
    ],
    [
        9, 10
    ],
    [
        "John", "Again"
    ],
    11
]
funcs = FunWithLists(my_list)  # TODO: Make this even more DRY
print("The old my_list: ")
print(my_list)
print("Flattened my_list: ")
funcs.flatten_it()  # flatten it
print(my_list)  # print it
print("Reversed and flattened my_list: ")
funcs.reverse_list()  # reverse the list
print(my_list)  # print it
print("Sorted and flattened my_list: ")
funcs.sort_list()
print(my_list)
print("The length of my_list: ")
print(funcs.length_of_list())
print("The amount of times \"Again\" appears in my_list: ")
print(funcs.count_in_list("Again"))
print("The index of \"Again\" in my_list is: ")
print(funcs.index_in_list("Again"))
print("Popping the last element off of my_list: ")
print(funcs.pop_from_list())
print("Now my_list will be cleared: ")
funcs.clear_list()
print(my_list)
