def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k <= x // d:
        ans = x - k * d
    else:
        ans = x % d
        if (k - x // d) % 2 == 1:
            ans = d - ans
    print(ans)
