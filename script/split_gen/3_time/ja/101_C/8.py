def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A # 1-indexed
    # A[i] <= A[i+1] <= ... <= A[i+K-1] となるような i が存在するか
    def check(x):
        for i in range(1, N-K+2):
            if A[i] <= x <= A[i+K-1]:
                return True
        return False
    # 二分探索
    ok = 0
    ng = N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    # 答えは A[i] が ok になるまでの操作回数
    ans = 0
    for i in range(1, N-K+2):
        if A[i] <= ok <= A[i+K-1]:
            ans += ok - A[i]
        else:
            ans += A[i+K-1] - A[i]
    print(ans)
