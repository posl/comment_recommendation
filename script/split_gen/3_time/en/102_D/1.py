def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = float('inf')
    for i in range(2, N - 1):
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < S[i + 1] - S[m]:
                l = m
            else:
                r = m
        ans = min(ans, max(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]) - min(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]))
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < S[i + 1] - S[m]:
                l = m
            else:
                r = m
        ans = min(ans, max(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]) - min(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]))
    print(ans)
