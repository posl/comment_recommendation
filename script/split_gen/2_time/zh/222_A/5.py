def add_zero(number):
    if number > 9999 or number < 0:
        return "ERROR"
    else:
        return "{:04d}".format(number)
print(add_zero(int(input())))
