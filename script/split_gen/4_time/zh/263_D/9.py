def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 0:
            if l + r < 0:
                ans += l + r
                l = 0
                r = 0
            else:
                ans += a[i]
        elif l + r < a[i]:
            ans += l + r
            l = 0
            r = 0
        else:
            ans += a[i]
            if l > r:
                l -= a[i]
            else:
                r -= a[i]
    print(ans)
