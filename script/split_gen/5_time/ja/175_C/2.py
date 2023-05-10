def solve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    k -= x // d
    x %= d
    if k % 2 == 0:
        print(x)
    else:
        print(d - x)
