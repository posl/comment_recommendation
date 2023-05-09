def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * ((n-i-1) * r + (i) * l) // n
        ans -= a[i] * ((n-i-1) * l + (i) * r) // n
    print(ans)
