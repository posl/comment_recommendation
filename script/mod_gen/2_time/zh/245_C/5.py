def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 二分探索
    def check(x):
        cnt = 0
        for i in range(N):
            cnt += abs(A[i] - x)
            cnt += abs(B[i] - x)
            cnt -= abs(A[i] - B[i])
        return cnt <= 2 * K
    # 二分探索
    ok = 0
    ng = 2 * 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print('Yes' if ok == 0 else 'No')

if __name__ == '__main__':
    solve()