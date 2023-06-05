def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    # 二分探索
    def isOK(x):
        # x分でクリアできるステージ数
        cnt = [0] * N
        # あとx分でクリアできるステージ数
        rest = [0] * N
        for i in range(N):
            cnt[i] = max(0, (x - B[i]) // A[i] + 1)
            rest[i] = max(0, (x - B[i]) % A[i])
        cnt.sort()
        # x分でクリアできるステージ数の合計
        total = sum(cnt)
        # あとx分でクリアできるステージ数の合計
        rest_total = sum(rest)
        return total >= X and rest_total <= x
    # 二分探索
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(10 ** 18, 0))

if __name__ == '__main__':
    main()