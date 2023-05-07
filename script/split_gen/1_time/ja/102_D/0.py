def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            ans = min(ans, max(S[i], S[j] - S[i], S[N] - S[j]) - min(S[i], S[j] - S[i], S[N] - S[j]))
    print(ans)
