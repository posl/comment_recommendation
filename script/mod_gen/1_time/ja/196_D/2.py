def f(h, w, a, b):
    if h < 2 or w < 2:
        return 1
    if a == 0:
        return f(h - 1, w, a, b) + f(h, w - 1, a, b)
    return f(h - 1, w, a, b) + f(h, w - 1, a, b) + f(h - 2, w, a - 1, b) + f(h, w - 2, a - 1, b)
h, w, a, b = map(int, input().split())
print(f(h, w, a, b))

if __name__ == '__main__':
    f()