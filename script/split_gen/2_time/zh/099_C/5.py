def getLeastTimes(n):
    if n <= 6:
        return n
    elif n <= 9:
        return 2
    else:
        return 1 + min(getLeastTimes(n-1), getLeastTimes(n-6), getLeastTimes(n-9))
