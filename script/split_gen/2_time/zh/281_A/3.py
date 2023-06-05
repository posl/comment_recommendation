def find_min_factorial(k):
    if k % 2 == 0:
        return 2
    elif k % 3 == 0:
        return 3
    elif k % 5 == 0:
        return 5
    else:
        return k
