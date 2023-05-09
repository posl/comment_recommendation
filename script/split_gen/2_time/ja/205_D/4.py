def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - (i + 1)
    for k in K:
        if k <= A[0]:
            print(k)
        elif k > A[-1]:
            print(A[-1] + k - N)
        else:
            ok = 0
            ng = N
            while ng - ok > 1:
                mid = (ok + ng) // 2
                if B[mid] < k:
                    ok = mid
                else:
                    ng = mid
            print(A[ok] + k - B[ok])
