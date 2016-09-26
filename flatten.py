def flatten_array(my_list):
    my_new_one = []
    i = 0
    for thing in my_list:
        if type(thing) is not str and \
           type(thing) is not int and \
           type(thing) is not float:
            for other in thing:
                my_new_one.append(other)
        else:
            my_new_one.append(thing)
    for more in my_new_one:
        try:
            my_list[i] = more
        except IndexError:
            my_list.append(more)
        i += 1
