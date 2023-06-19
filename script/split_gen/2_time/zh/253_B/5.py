def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    #print(s)
    #找到两个棋子的位置
    pos = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                pos.append([i, j])
    #print(pos)
    #计算两个棋子之间的距离
    dis = abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1])
    #print(dis)
    #计算两个棋子之间的距离
    if dis == 1:
        print(1)
    elif dis == 2:
        print(2)
    else:
        print(dis - 1)
