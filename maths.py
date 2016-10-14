my_pi = 3.1415926535897932384626433832795028841971693993751
infinite = float("inf")
my_e = 2.71828182845904523536028747135266249775724709369995
int_max = 9223372036854775807
int_min = -9223372036854775808


def x_is_greater_than_zero(x):
    """
    Returns True if X and Y are greater than 0.
    """
    if x > 0:
        return True
    else:
        return False


def x_abs(x):
    """
    Returns the absolute value of X.
    """
    if x < 0:
        return -x
    else:
        return x


def power(x, y):
    """
    X ^ Y
    """
    if x_is_greater_than_zero(x):
        return x ** y


def x_is_nan(x):
    """
    Returns True if X is Not A Number.
    """
    try:
        int(x)
        return False
    except ValueError:
        return True


def square_root(x, y):
    """
    Returns the square root of X by the power of Y
    """
    if x_is_greater_than_zero(x):
        return x ** 1.0 / float(y)


def x_to_degrees(x):
    """
    We trust you won't misuse this.
    """
    if x <= 2:
        return x * (180.0 / my_pi)
    else:
        return x


def x_to_radians(x):
    """
    Converts degrees to radians.
    """
    return x * (my_pi / 180.0)


def x_round(x):
    """
    Rounds a float.
    """
    local_x = str(x)
    for i in range(0, len(local_x)):
        if local_x[i] is ".":
            dec_to_round = int(local_x[i + 1])
            break
        elif i == len(local_x) - 1:
            dec_to_round = 0
    if dec_to_round > 4 and not x_is_neg(x):
        return int(float(local_x) + 1)
    else:
        if dec_to_round < 5:
            return int(float(local_x))
        else:
            return int(float(local_x) - 1)


def x_is_neg(x):
    """
    Returns True when X is negative.
    """
    if x < 0:
        return True
    else:
        return False


def greatest_common_divisor(x, y):
    """
    Returns the greatest common divisor of both X and Y,
    such that the gcd is not X or Y.
    """
    i = 1
    while True:
        if x % i == 0 and y % i == 0 and \
                i != x and i != y:
            local_z = i
        elif x < 1 or y < 1:
            return "X or Y needs to be a bigger number."
        elif i > x and i > y:
            break
        i += 1
    return local_z


def x_is_finite(x):
    """
    Returns True if X is not infinite or 0
    """
    if x != float("inf") and x != 0:
        return True
    else:
        return False

# TODO: Make more methods

print("X is greater than 0: ")
print(x_is_greater_than_zero(-1.6))
print("X absolute value is: ")
print(x_abs(-1.6))
print("X is not a number: ")
print(x_is_nan("Jake"))
print("X ^ Y is: ")
print(power(-1.6, 18))
print("X to the square root of Y is: ")
print(square_root(6, 2))
print("X to radians: ")
print(x_to_radians(180))
print("X to degrees: ")
print(x_to_degrees(2))
print("X rounded: ")
print(x_round(-1.6))
print("X is negative: ")
print(x_is_neg(-1.6))
print("The GCD of X and Y: ")
print(greatest_common_divisor(18, 6))
print("X is finite: ")
print(x_is_finite(-1.6))
