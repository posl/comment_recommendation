def f(n):
    if n == 0:
        return 1
    else:
        return f(n//2) + f(n//3)
N = int(input())
print(f(N))
