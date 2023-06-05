def f(x):
    if x == 0:
        return 0
    return 2*f(x//2)+1
h = int(input())
print(f(h))
