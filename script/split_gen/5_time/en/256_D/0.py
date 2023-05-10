def solve():
    N = int(input())
    L = []
    R = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L, R)
    ans = 0
    for i in range(N):
        ans += R[i] - L[i] + 1
    print(ans)
solve()
