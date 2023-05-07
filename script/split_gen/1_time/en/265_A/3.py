def buy_apple(x, y, n):
    if n % 3 == 0:
        return (n // 3) * y
    elif n % 3 == 1:
        return (n // 3) * y + x
    else:
        return (n // 3) * y + (n % 3) * x
