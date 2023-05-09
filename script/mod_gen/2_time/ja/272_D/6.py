def main():
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    # (1,1)からの距離
    d = [[10**9] * N for _ in range(N)]
    d[0][0] = 0
    # (1,1)からの距離がMの平方根となるマスの座標を求める
    for i in range(N):
        for j in range(N):
            if (i**2+j**2) == M:
                ans[i][j] = 1
                d[i][j] = 1
    # 1マスずつ距離を求める
    for i in range(N):
        for j in range(N):
            if i+1 < N:
                if d[i+1][j] > d[i][j] + 1:
                    d[i+1][j] = d[i][j] + 1
            if j+1 < N:
                if d[i][j+1] > d[i][j] + 1:
                    d[i][j+1] = d[i][j] + 1
            if i-1 >= 0:
                if d[i-1][j] > d[i][j] + 1:
                    d[i-1][j] = d[i][j] + 1
            if j-1 >= 0:
                if d[i][j-1] > d[i][j] + 1:
                    d[i][j-1] = d[i][j] + 1
    for i in range(N):
        for j in range(N):
            if d[i][j] == 10**9:
                d[i][j] = -1
    for i in range(N):
        for j in range(N):
            if ans[i][j] == 1:
                ans[i][j] = d[i][j]
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()