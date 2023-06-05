def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        c = min(a[i], b[i])
        ans += c
        a[i] -= c
        b[i] -= c
        d = min(a[i+1], b[i])
        ans += d
        a[i+1] -= d
        b[i] -= d
    print(ans)
