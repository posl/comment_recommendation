def main():
    # 从标准输入读取数据
    s = []
    for i in range(10):
        s.append(input())
    # 求解
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i+1,j+1)
                exit()
