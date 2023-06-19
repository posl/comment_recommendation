def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    ans = 0
    for i in range(n - 1):
        ans += abs(a[i] - a[i + 1])
    for i in range(q):
        if i == 0:
            ans += abs(a[0] - x[i])
            ans += abs(a[-1] - x[i])
        else:
            ans -= abs(a[i] - a[i - 1])
            ans -= abs(a[i] - a[i + 1])
            ans += abs(a[i - 1] - x[i])
            ans += abs(a[i + 1] - x[i])
        print(ans)
        a[i] = x[i]
    return
