def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A = [0] + A + [10**18]
    for k in K:
        ok = 0
        ng = N+2
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if k <= A[mid] - A[mid-1] - 1:
                ng = mid
            else:
                k -= A[mid] - A[mid-1] - 1
                ok = mid
        print(A[ok] + k)

if __name__ == '__main__':
    main()