def change(n):
    if n % 1000 == 0:
        return 0
    else:
        return 1000 - n % 1000
