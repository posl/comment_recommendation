def solve(x, k, d):
    x = abs(x)
    if x / d > k:
        return x - k * d
    else:
        k -= x / d
        x %= d
        if k % 2 == 0:
            return x
        else:
            return d - x
x, k, d = map(int, raw_input().split())
print solve(x, k, d)
