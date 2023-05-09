def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    def check(x):
        cnt = 0
        for i in range(N):
            total = sum(P[i])
            if total + x >= 300 * 3:
                cnt += 1
        return cnt >= K
    ok = 300
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
