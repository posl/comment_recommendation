def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = A[i] - A[i - 1] - 1
    for i in range(N):
        B[i + 1] += B[i]
    for k in K:
        if k > B[N]:
            print(A[-1] + k - B[N])
            continue
        ok = 0
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] >= k:
                ng = mid
            else:
                ok = mid
        print(A[ok] + k - B[ok])
