def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [0] + P
    for i in range(1, N+1):
        P[i] += P[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (P[i+K] - P[i]) / 2 + P[i])
    print(ans)

if __name__ == '__main__':
    solve()