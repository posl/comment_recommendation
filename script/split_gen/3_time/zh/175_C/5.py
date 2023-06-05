def solve(x, k, d):
    x = abs(x)
    if x // d >= k:
        return x - k * d
    else:
        y = x % d
        k -= x // d
        if k % 2 == 0:
            return y
        else:
            return d - y
x, k, d = map(int, input().split())
print(solve(x, k, d))
