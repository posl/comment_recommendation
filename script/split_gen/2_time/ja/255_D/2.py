def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    B.sort()
    B = [0] + B
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + B[i]
    for x in X:
        ok = 0
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] <= x:
                ok = mid
            else:
                ng = mid
        ans = (x + 1) * ok - S[ok]
        ans += S[N] - S[ok] - (x + 1) * (N - ok)
        print(ans)
