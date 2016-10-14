from sys import stdout
from my_time import time_it


def figure_it():
    """
    Figures out the user entered password.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789" \
            "0!@#$%^&*()_+-={}|[]\\:\"',./<>?`~ "
    _new = []
    thing_to_search = raw_input("Enter your password: ")
    for i in range(0, len(thing_to_search)):
        for x in range(0, len(chars)):
            if chars[x] == thing_to_search[i]:
                _new.append(chars[x])
                stdout.write(chars[x])


print(time_it(figure_it))
print
print("The computer has figured out your password.")
