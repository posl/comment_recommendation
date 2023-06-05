def main():
    h, w, n = map(int, input().split())
    # print(h, w, n)
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    # print(ab)
    # 1. 生成一个h*w的矩阵
    # 2. 依次填入ab中的数字
    # 3. 从上往下，从左往右，填入数字，如果有数字，就跳过
    # 4. 如果某一行或者某一列没有数字，就把这一行或者这一列的数字都清空，然后把剩下的数字往上或者往左移动，填补空缺
    # 5. 重复3，4
    matrix = [[0 for _ in range(w)] for _ in range(h)]
    # print(matrix)
    for i in range(n):
        a, b = ab[i]
        matrix[a-1][b-1] = i + 1
    # print(matrix)
    # 从上往下
    for i in range(h):
        # 从左往右
        for j in range(w):
            if matrix[i][j] == 0:
                continue
            else:
                print(i+1, j+1)

if __name__ == '__main__':
    main()