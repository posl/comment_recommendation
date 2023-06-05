def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 0:
            if l > 0:
                ans += l
                l = 0
            else:
                ans += a[i]
        elif a[i] > 0:
            if r > 0:
                ans += r
                r = 0
            else:
                ans += a[i]
        else:
            ans += l + r
            l = r = 0
    print(ans)
