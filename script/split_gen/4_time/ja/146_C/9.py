def main():
    A,B,X = map(int,input().split())
    # 最大の整数を買うことができるかどうかを判定する関数
    def is_ok(n):
        if A * n + B * len(str(n)) <= X:
            return True
        else:
            return False
    # 二分探索
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    # ng = 0
    # ok = 10**9+1
    print(meguru_bisect(0, 10**9+1))
