def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 计算
    # 遍历9*9的格子
    # 如果该格子是#，则遍历该格子的右侧和下侧的格子，如果都是#，则答案+1
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                if j < 8 and s[i][j + 1] == "#" and i < 8 and s[i + 1][j] == "#":
                    ans += 1
    # 输出
    print(ans)
