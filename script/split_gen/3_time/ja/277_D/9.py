def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] + a[i+1] if a[i] + a[i+1] < m else a[i] + a[i+1] - m
        if a[i] + a[i+1] >= m:
            a[i+1] = a[i] + a[i+1] - m
    print(ans)
