def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    for i in range(N):
        ans += (S[N] - S[i]) % M
    print(ans)
