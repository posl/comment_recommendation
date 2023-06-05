def solve():
    N, X = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    # print(N, X)
    # print(AB)
    # print(A)
    # print(B)
    # print()
    # 二分探索
    # ok: X分でクリアできるか
    # ng: X分でクリアできない
    ok = 0
    ng = 10**18
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print(mid)
        # print(f(ok), f(mid), f(ng))
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    solve()