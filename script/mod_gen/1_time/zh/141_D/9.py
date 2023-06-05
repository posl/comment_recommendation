def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    # 二分探索
    def is_ok(x):
        # 二分探索の判定部分
        cnt = 0
        for a in A:
            if a < x // 2:
                break
            cnt += min(a, x // 2)
        return cnt >= M * x
    def meguru_bisect(ng, ok):
        # 二分探索
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(0, 10 ** 18))

if __name__ == '__main__':
    solve()