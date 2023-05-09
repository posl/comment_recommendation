def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    zero_count = A.count(0)
    if zero_count > 0:
        if K <= zero_count * (zero_count - 1) // 2:
            print(0)
        elif K <= zero_count * (N - zero_count):
            print(0)
        else:
            K -= zero_count * (N - zero_count)
            A = [x for x in A if x != 0]
            N -= zero_count
    if K == 0:
        print(0)
        return
    def is_ok(x):
        cnt = 0
        for i in range(N):
            if A[i] < 0:
                for j in range(i + 1, N):
                    if A[i] * A[j] <= x:
                        break
                    cnt += 1
            else:
                for j in range(i + 1, N):
                    if A[i] * A[j] <= x:
                        cnt += N - j
                        break
        return cnt >= K
    ng = -10 ** 18
    ok = 10 ** 18
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
