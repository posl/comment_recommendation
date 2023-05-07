def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K - 1])
        return
    if A[-1] <= 0:
        print(A[N - K])
        return
    if K == N * (N - 1) // 2:
        print(A[-1] * A[-2])
        return
    def is_ok(x):
        cnt = 0
        j = N - 1
        for i in range(N):
            while j > i and A[i] * A[j] > x:
                j -= 1
            cnt += j - i
        return cnt >= K
    ng = -1
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()