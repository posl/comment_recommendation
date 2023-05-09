def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    r = 0
    ans = 0
    for l in range(N):
        while r < N and S[r + 1] - S[l] < K:
            r += 1
        if S[r + 1] - S[l] == K:
            ans += 1
    print(ans)
