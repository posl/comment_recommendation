def f(x):
    if x < 2:
        return 1
    else:
        return f(x//2) + f(x//3)
N = int(input())
print(f(N))
