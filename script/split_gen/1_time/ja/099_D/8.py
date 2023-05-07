def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # D[i][j] = iからjに塗り替えるときの違和感
    # c[i][j] = (i,j)の色
    # color[i] = iの色を塗り替えるときの違和感の和
    color = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            color[(i+j)%3][c[i][j]-1] += 1
    ans = 10**10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    tmp = 0
                    for l in range(C):
                        tmp += D[l][i]*color[0][l]
                        tmp += D[l][j]*color[1][l]
                        tmp += D[l][k]*color[2][l]
                    ans = min(ans, tmp)
    print(ans)
