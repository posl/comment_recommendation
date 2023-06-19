def f(h, w, a, b):
    if a == 0 or b == 0:
        return 1
    if h == 1:
        return f(w, h, b, a)
    return f(h-1, w, a-1, b) + f(h-1, w, a, b-1)
h, w, a, b = map(int, input().split())
print(f(h, w, a, b))
