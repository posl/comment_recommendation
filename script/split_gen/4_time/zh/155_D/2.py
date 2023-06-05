def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # print(n, k)
    # print(a)
    # 二分探索
    def is_ok(x):
        # x以上のペアの数がk以上かどうか
        cnt = 0
        for i in range(n):
            if a[i] >= 0:
                # a[i]以上のペアの数
                l = i
                r = n
                while r-l>1:
                    m = (l+r)//2
                    if a[i] * a[m] <= x:
                        l = m
                    else:
                        r = m
                cnt += n - l - 1
            else:
                # a[i]以下のペアの数
                l = -1
                r = i
                while r-l>1:
                    m = (l+r)//2
                    if a[i] * a[m] <= x:
                        r = m
                    else:
                        l = m
                cnt += l + 1
        # print(x, cnt)
        return cnt >= k
    # 二分探索
    # 求める値はx
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    # print(is_ok(6))
    # print(is_ok(7))
    # print(is_ok(8))
    # print(is_ok(9))
    # print(is_ok(10))
    # print(is_ok(11))
    # print(is_ok(12))
    # print(is_ok(13))
    # print(is_ok(14))
    # print(is_ok(15))
    # print(is_ok(16))
    # print(is_ok(17))
    # print(is_ok(18))
    # print(is_ok(19))
    # print(is_ok(20))
    # print(is_ok(21))
    # print(is_ok(22))
    # print(is_ok(23))
    # print(is_ok(24))
    # print(is_ok(25))
    # print(is
