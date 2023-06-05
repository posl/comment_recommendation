def main():
    # 读取输入
    s = []
    for i in range(10):
        s.append(input())
    # 计算
    row = 0
    col = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                row = i
                col = j
                break
    # 输出
    print(row+1, col+1)
    print(row+2, col+2)
