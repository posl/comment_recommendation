def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    ans = 10**18
    for i in range(2, N-1):
        L = S[i]
        R = S[N] - S[i]
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < L // 2:
                l = m
            else:
                r = m
        if abs(L - 2 * S[l]) <= abs(L - 2 * S[r]):
            ans = min(ans, max(L - S[l], S[l], R - S[l], S[l]) - min(L - S[l], S[l], R - S[l], S[l]))
        else:
            ans = min(ans, max(L - S[r], S[r], R - S[r], S[r]) - min(L - S[r], S[r], R - S[r], S[r]))
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < R // 2:
                l = m
            else:
                r = m
        if abs(R - 2 * S[l]) <= abs(R - 2 * S[r]):
            ans = min(ans, max(L - S[l], S[l], R - S[l], S[l]) - min(L - S[l], S[l], R - S[l], S[l]))
        else:
            ans = min(ans, max(L - S[r], S[r], R - S[r], S[r]) - min(L - S[r], S[r], R - S[r], S[r]))
    print(ans)
