def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    def f(x):
        return x - sum(x // a for a in A)
    ans = []
    for k in K:
        ng = 0
        ok = 10 ** 18 + 1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if f(mid) < k:
                ng = mid
            else:
                ok = mid
        ans.append(ok)
    print(*ans, sep='
')
