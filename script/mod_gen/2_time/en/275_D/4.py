def f(k):
    if k == 0:
        return 1
    return f(k//2) + f(k//3)
N = int(input())
print(f(N))
