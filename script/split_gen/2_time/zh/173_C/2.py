def f(h, w, k):
    if k == 0:
        return 1
    if h == 0 or w == 0:
        return 0
    return f(h - 1, w, k) + f(h, w - 1, k) + f(h - 1, w - 1, k - 1) * (h * w - k)
h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
print(f(h, w, k))
