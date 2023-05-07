def main():
    # input
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    # compute
    ans = [0] * Q
    for i in range(Q):
        for j in range(M):
            if LR[j][0] <= PQ[i][0] and PQ[i][1] <= LR[j][1]:
                ans[i] += 1
    # output
    for i in range(Q):
        print(ans[i])
