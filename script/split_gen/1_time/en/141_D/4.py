def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= m:
            m -= a[i]
        else:
            ans += a[i] - m
            m = 0
    print(ans)
