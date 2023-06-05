def main():
    # 读取输入
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    # 计算可见方块的数量
    count = 1
    for i in range(X - 2, -1, -1):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for j in range(Y - 2, -1, -1):
        if S[X - 1][j] == '#':
            break
        count += 1
    for j in range(Y, W):
        if S[X - 1][j] == '#':
            break
        count += 1
    # 输出答案
    print(count)
