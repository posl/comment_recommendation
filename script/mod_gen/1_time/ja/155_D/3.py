def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    def calc(x):
        cnt = 0
        for i in range(1, N + 1):
            if A[i] < 0:
                cnt += bisect_left(A, -(-x // A[i]), i + 1, N + 1) - (i + 1)
            else:
                cnt += N - bisect_left(A, x // A[i], i + 1, N + 1) + 1
        return cnt
    ng = -10 ** 18 - 1
    ok = 10 ** 18 + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if calc(mid) >= K:
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()