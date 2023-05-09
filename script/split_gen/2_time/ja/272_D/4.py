def main():
    N,M = map(int,input().split())
    D = [[10**9]*N for _ in range(N)]
    D[0][0] = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i-k)**2+(j-l)**2 == M:
                        D[i][j] = min(D[i][j],D[k][l]+1)
    for i in range(N):
        print(*D[i])
