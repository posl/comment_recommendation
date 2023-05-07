def main():
    N = int(input())
    data = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        data.append((x, y, p))
    #d[i][j]: i番目のジャンプ台からj番目のジャンプ台に移動するために必要な最小のS
    d = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                d[i][j] = 0
            elif data[i][2] * d[i][i] >= abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1]):
                d[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, d[i][j])
    print(ans)

if __name__ == '__main__':
    main()