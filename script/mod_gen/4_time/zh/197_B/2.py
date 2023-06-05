def main():
    # 读取数据
    H, W, X, Y = map(int, input().split())
    X = X - 1
    Y = Y - 1
    S = [input() for i in range(H)]
    # 计算可见方块数
    count = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '.':
            count += 1
        else:
            break
    for i in range(X + 1, H):
        if S[i][Y] == '.':
            count += 1
        else:
            break
    for j in range(Y - 1, -1, -1):
        if S[X][j] == '.':
            count += 1
        else:
            break
    for j in range(Y + 1, W):
        if S[X][j] == '.':
            count += 1
        else:
            break
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()