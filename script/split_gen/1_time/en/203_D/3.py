def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    H = sorted([A[i][j] for i in range(N) for j in range(N)])
    def check(x):
        cnt = 0
        for i in range(N):
            for j in range(N):
                if A[i][j] > x:
                    break
                for k in range(i, N):
                    for l in range(j, N):
                        if A[k][l] > x:
                            break
                        cnt += 1
                        if cnt >= K * K:
                            return True
        return False
    ng = -1
    ok = 10 ** 9 + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(H[mid]):
            ok = mid
        else:
            ng = mid
    print(H[ok])
