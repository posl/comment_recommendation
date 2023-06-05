def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < m:
            ans += m - a[i]
        else:
            ans += a[i] % m
    print(ans)
