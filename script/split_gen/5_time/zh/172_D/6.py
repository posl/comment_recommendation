def f(x):
    return sum([1 for k in range(1, x+1) if x % k == 0])
