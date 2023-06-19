def f(n):
    if n == 0:
        return 1
    else:
        return f(int(n/2)) + f(int(n/3))
n = int(input())
print(f(n))
