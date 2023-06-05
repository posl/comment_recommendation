def f(k):
    if k == 0:
        return 1
    else:
        return k * f(k-1)
n = int(input())
print(f(n))
