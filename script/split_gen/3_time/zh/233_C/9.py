def solve():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 二分探索
    def check(x):
        cnt = 0
        for a in A:
            for ai in a:
                if ai * x >= X:
                    cnt += 1
                    break
        return cnt == N
    ok = 0
    ng = 10 ** 9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    # 二分探索終了後、ok は条件を満たす最小の値となっている。
    ans = 0
    for a in A:
        for ai in a:
            if ai * ok >= X:
                ans += 1
                break
    print(ans)
