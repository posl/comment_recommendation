def blue_ball(n, a, b):
    if n == 1:
        return a
    elif n == 2:
        return a+b
    else:
        return blue_ball(n-1, a, b) + blue_ball(n-2, a, b)
