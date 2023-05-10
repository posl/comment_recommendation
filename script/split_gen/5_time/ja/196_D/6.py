def calc(h, w, a, b):
    if h == 0 or w == 0:
        return 1
    if (h, w) in memo:
        return memo[(h, w)]
    ret = 0
    if a >= 2 and w >= 2:
        ret += calc(h, w-2, a-2, b)
    if a >= 1 and b >= 1 and w >= 1:
        ret += calc(h-1, w-1, a-1, b-1)
    if b >= 2 and h >= 2:
        ret += calc(h-2, w, a, b-2)
    memo[(h, w)] = ret
    return ret
H, W, A, B = map(int, input().split())
memo = {}
print(calc(H, W, A, B))
