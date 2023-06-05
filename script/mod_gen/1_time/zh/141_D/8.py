def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 二分探索
    def is_ok(arg):
        cnt = 0
        for i in range(n):
            cnt += max(0, a[i] - arg // 2)
        return cnt >= m
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(0, 10 ** 9 + 1))

if __name__ == '__main__':
    main()