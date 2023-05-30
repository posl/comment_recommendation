def f(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    return f(x//2) + f(x//3)
N = int(input())
print(f(N))
