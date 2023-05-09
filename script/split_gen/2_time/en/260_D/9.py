def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # init
    tbl = [0] * (N + 1)
    for i in range(N):
        tbl[P[i]] = i
    # solve
    ans = [-1] * N
    for x in range(1, N + 1):
        if ans[x - 1] >= 0:
            continue
        # x is not eaten
        i = tbl[x]
        for j in range(i, i + K):
            if j >= N:
                break
            ans[P[j] - 1] = x
    # output
    for i in range(N):
        print(ans[i])
