def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 找到两个棋子的位置
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                p1 = (i, j)
                break
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if S[i][j] == 'o':
                p2 = (i, j)
                break
    # 通过计算两个棋子之间的距离来确定答案
    if p1[0] == p2[0]:
        print(abs(p1[1] - p2[1]))
    elif p1[1] == p2[1]:
        print(abs(p1[0] - p2[0]))
    else:
        print(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + 1)
