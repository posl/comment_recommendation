def solve():
    N, D = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(N)]
    LRs.sort()
    LRs.append([10**9+1, 10**9+1])
    ans = 0
    p = 0
    for i in range(N):
        L, R = LRs[i]
        while p < N and LRs[p][0] <= R:
            p += 1
        ans += max(0, p-i-1)
    print(ans)
solve()
