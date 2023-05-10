def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            if S[j] - S[i] == K:
                ans += 1
    print(ans)
