def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(input())
    # 找到最左边的#和最右边的#
    left = 10
    right = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                left = min(left, j)
                right = max(right, j)
    # 找到最上面的#和最下面的#
    top = 10
    bottom = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                top = min(top, i)
                bottom = max(bottom, i)
    # 根据最左边的#和最右边的#，找到A和B
    A = 10 - (right - left + 1) + 1
    B = 10
    # 根据最上面的#和最下面的#，找到C和D
    C = 10 - (bottom - top + 1) + 1
    D = 10
    # 打印结果
    print(A, B)
    print(C, D)
