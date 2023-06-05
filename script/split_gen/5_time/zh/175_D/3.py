def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N):
        v = i
        s = 0
        t = 0
        while True:
            v = P[v] - 1
            s += C[v]
            t += 1
            if v == i:
                break
            if t == K:
                break
        if s > ans:
            ans = s
    print(ans)
solve()
