def get_candy():
    n = int(input())
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n-1
