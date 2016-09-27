def depth(of_list):
    if isinstance(of_list, list) and len(of_list) > 0:
        new_depth = 1 + max([depth(item) for item in of_list])
        return new_depth
    else:
        return 0


def reverse_list(the_list):
    the_list[::-1] = the_list


def flatten_2d(a_list):
    my_new_one = []
    i = 0
    for first_d in my_list:
        if type(first_d) is not str and \
                    type(first_d) is not int and \
                    type(first_d) is not float:
            for second_d in first_d:
                my_new_one[len(my_new_one):] = [second_d]
        else:
            my_new_one[len(my_new_one):] = [first_d]
    for more in my_new_one:
        try:
            a_list[i] = more
        except IndexError:
            a_list[len(a_list):] = [more]
        i += 1


def flatten_it(new_list):
    for number in range(0, depth(new_list)):
        flatten_2d(new_list)

# below is an example N-dimensional list

my_list = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        ["John", "Deer"],
        [[[[[["Jane", "Doe"]]]]]]
    ],
    [
        9, 10
    ],
    [
        "John", "Again"
    ],
    11
]
print(depth(my_list))  # first print the depth of the list
flatten_it(my_list)  # flatten it
print(my_list)  # print it
reverse_list(my_list)  # reverse the list
print(my_list)  # print it
