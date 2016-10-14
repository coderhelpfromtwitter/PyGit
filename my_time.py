from time import clock


def time_it(function_call):
    start = clock()
    function_call()
    print
    finish = clock()
    return finish - start
