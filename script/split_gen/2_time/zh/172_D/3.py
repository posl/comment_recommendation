def f(x):
    n = 0
    for i in range(1,x+1):
        if x % i == 0:
            n += 1
    return n
