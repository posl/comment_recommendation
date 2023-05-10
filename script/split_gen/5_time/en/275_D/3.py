def f(k):
    if k == 0:
        return 1
    else:
        return f(k//2) + f(k//3)
n = int(input())
print(f(n))
