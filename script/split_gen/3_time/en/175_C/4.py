def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    ans = 0
    if x - k * d >= 0:
        ans = x - k * d
    else:
        if (k - x // d) % 2 == 0:
            ans = x % d
        else:
            ans = d - x % d
    print(ans)
