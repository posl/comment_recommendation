def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(list(input()))
    # 从上往下找
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i+1, j+1, end=' ')
                break
        if s[i][j] == '#':
            break
    # 从下往上找
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if s[i][j] == '#':
                print(i+1, j+1)
                break
        if s[i][j] == '#':
            break
