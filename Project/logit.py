from datetime import date, datetime


def print_to_log(error):
    """
    Prints errors to a log file.
    """
    fp = open("Project/logs.txt", "a+")
    fp.write(str(date.today()) + " - " + str(datetime.now()) +
             " [ " + str(error) + " ]\n")
    fp.close()
