def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = [p-1 for p in P]
    YY = sorted([(y, i) for i, y in enumerate(Y)])
    PP = sorted([(p, i) for i, p in enumerate(P)])
    ans = [0] * M
    j = 0
    for i in range(M):
        while j < M and YY[j][0] <= Y[PP[i][1]]:
            ans[YY[j][1]] = str(PP[i][0]+1).zfill(6) + str(j+1).zfill(6)
            j += 1
    for i in range(M):
        print(ans[i])
