def f(h):
    if h == 1:
        return 1
    else:
        return 2*f(h//2) + 1
h = int(input())
print(f(h))
