def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色ごとにマスの個数を数える
    cnt = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%3][c[i][j]-1] += 1
    # 3色のうち2色を選び、それぞれの色に塗り替えるときの違和感の合計の最小値を求める
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if k == i or k == j:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i]*cnt[0][l]
                    tmp += D[l][j]*cnt[1][l]
                    tmp += D[l][k]*cnt[2][l]
                ans = min(ans, tmp)
    print(ans)
