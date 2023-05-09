def f(x):
    if x == 0:
        return 0
    else:
        return 1 + 2 * f(x//2)
H = int(input())
print(f(H))
