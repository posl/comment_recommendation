def func(n):
    for i in range(100000):
        if i**3 > n:
            return i
    return -1
n = int(input())
c = func(n)
