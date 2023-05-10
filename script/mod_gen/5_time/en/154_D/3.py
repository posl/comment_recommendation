def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + P[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (S[i+K]-S[i])/2)
    print(ans)

if __name__ == '__main__':
    solve()