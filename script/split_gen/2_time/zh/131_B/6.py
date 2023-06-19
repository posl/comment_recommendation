def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        ans += l + i - 1
    if ans > 0:
        ans -= l + n - 1
    elif ans < 0:
        ans -= l
    print(ans)
