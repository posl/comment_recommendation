def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        l, r = -1, -1
        for i in range(n):
            if h[i] > 0 and l == -1:
                l = i
            if h[i] == 0 and l != -1:
                r = i - 1
                break
        if r == -1:
            r = n - 1
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)
