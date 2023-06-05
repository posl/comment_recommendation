def solve(n,k,a):
    # 二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る
        # ここで条件式を書く
        # return mid >= 0
        # ここで条件式を書く
        return sum(max(0, a_i - arg) for a_i in a) <= k
    # 二分探索
    def meguru_bisect(ng, ok):
        # okとngのどちらが大きいかわからないことを考慮
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    # 解の存在範囲を初期化
    ok = max(a)
    ng = 0
    # 二分探索
    ans = meguru_bisect(ng, ok)
    return ans

if __name__ == '__main__':
    solve()