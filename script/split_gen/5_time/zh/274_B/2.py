def problem274_b():
    #输入
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    #处理
    for i in range(H):
        count = 0
        for j in range(W):
            if C[i][j] == '#':
                count += 1
        print(count)
