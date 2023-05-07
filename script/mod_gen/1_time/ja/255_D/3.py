def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    B.sort()
    B_cumsum = [0] * (N + 1)
    for i in range(N):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]
    for x in X:
        ok = N
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if B[mid] <= x:
                ok = mid
            else:
                ng = mid
        print(N * x + B_cumsum[ok] - B_cumsum[0] - ok * (ok - 1) // 2)

if __name__ == '__main__':
    main()