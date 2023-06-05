def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(0, min(K+1, N+1)):
        for right in range(0, min(K+1-left, N+1)):
            now = V[:left] + V[N-right:]
            now.sort()
            ans = max(ans, sum(now[max(0, K-left-right):]))
    print(ans)
