def main():
    import sys
    import math
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    def is_ok(R):
        # 人iが光iに照らされるかどうか
        is_lit = [False] * N
        for i in range(K):
            is_lit[A[i]-1] = True
        # 光iが人jに照らすかどうか
        is_light = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if (X[i]-X[j])**2 + (Y[i]-Y[j])**2 <= R**2:
                    is_light[i][j] = True
        # 光iが人jに照らすかどうかでグループ化
        group = [0] * N
        group_num = 0
        for i in range(N):
            if is_lit[i]:
                group[i] = group_num
                group_num += 1
            else:
                for j in range(i):
                    if is_light[j][i]:
                        group[i] = group[j]
                        break
        # 人iが光iに照らされるかどうか
        for i in range(N):
            for j in range(N):
                if group[i] == group[j]:
                    is_lit[j] = is_lit[j] or is_light[i][j]
        return all(is_lit)
    # 二分探索
    ng = 0
    ok = 2*10**5
    while abs(ok-ng) > 10**-5:
        mid = (ok+ng)/2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
