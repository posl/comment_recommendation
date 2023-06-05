def f(a, b):
    if a == b:
        return a
    else:
        if a%2 == 1:
            return a^f(a+1, b)
        else:
            return f(a+1, b)
