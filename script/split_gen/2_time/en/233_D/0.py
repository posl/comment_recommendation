def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    S = [s - K for s in S]
    S.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)
