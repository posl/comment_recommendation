def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(max(a[i], l), r)
        a[i] = max(a[i], l)
        if a[i] > r:
            a[i+1] += a[i] - r
            a[i] = r
    ans += min(max(a[n-1], l), r)
    print(ans)
