from datetime import date, datetime


def print_to_log(error_log):
    fp = open("logs.txt", "a")
    text_to_write = str(date.today()) + " - " + str(datetime.now()) + " [ " + \
        str(error_log) + " ]\n"
    fp.write(text_to_write)
