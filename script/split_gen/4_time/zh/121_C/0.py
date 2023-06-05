def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 二分法
    def is_ok(x):
        # x円でM本以上買えるか？
        # x円で買える本数を計算
        num = 0
        for i in range(N):
            if A[i] > x:
                continue
            num += (x - A[i]) // B[i] + 1
        return num >= M
    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    print(meguru_bisect(0, 10 ** 18 + 1))
main()
