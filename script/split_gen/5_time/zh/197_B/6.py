def problem197_b():
    # 读入数据
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    # 计算答案
    ans = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for i in range(X, H):
        if S[i][Y-1] == '#':
            break
        ans += 1
    for j in range(Y-2, -1, -1):
        if S[X-1][j] == '#':
            break
        ans += 1
    for j in range(Y, W):
        if S[X-1][j] == '#':
            break
        ans += 1
    # 输出答案
    print(ans)
