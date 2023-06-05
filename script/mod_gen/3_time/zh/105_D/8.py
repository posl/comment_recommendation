def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = A[i] % M
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
        S[i + 1] %= M
    S.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
main()
