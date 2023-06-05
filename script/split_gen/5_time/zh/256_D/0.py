def solve():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    cur = 0
    for i in range(N):
        if cur < L[i]:
            ans += 1
            cur = R[i]
        else:
            cur = max(cur, R[i])
    ans += 1
    print(ans)
solve()
