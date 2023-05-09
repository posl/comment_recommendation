def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(r, l)
        if l <= r:
            r -= l
        else:
            l -= r
    ans += a[-1] + min(l, r)
    print(ans)
