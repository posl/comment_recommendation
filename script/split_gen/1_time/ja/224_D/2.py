def main():
    M = int(input())
    G = [[0]*9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] = 1
        G[v-1][u-1] = 1
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    ans = 10**10
    for i in range(9):
        for j in range(i+1, 9):
            for k in range(j+1, 9):
                for l in range(k+1, 9):
                    for m in range(l+1, 9):
                        for n in range(m+1, 9):
                            for o in range(n+1, 9):
                                for r in range(o+1, 9):
                                    for s in range(r+1, 9):
                                        P = [i, j, k, l, m, n, o, r, s]
                                        for t in range(9):
                                            if t not in P:
                                                P.append(t)
                                        flg = True
                                        for t in range(8):
                                            if G[P[t]][P[t+1]] == 0:
                                                flg = False
                                                break
                                        if flg:
                                            cnt = 0
                                            for t in range(8):
                                                if p[t] != P[t]:
                                                    cnt += 1
                                            ans = min(ans, cnt)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
