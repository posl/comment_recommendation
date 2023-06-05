def main():
    # 读取数据
    line1 = input().split()
    line2 = input().split()
    n = int(line1[0])
    a = int(line1[1])
    b = int(line1[2])
    p = int(line2[0])
    q = int(line2[1])
    r = int(line2[2])
    s = int(line2[3])
    # 初始化
    row = [0 for i in range(n)]
    col = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
        row[i] = 1
        col[i] = 1
        left[i] = 1
        right[i] = 1
    # 横向
    for i in range(1, n):
        if i <= a - 1:
            row[i] = 1
        else:
            row[i] = 0
    # 纵向
    for i in range(1, n):
        if i <= b - 1:
            col[i] = 1
        else:
            col[i] = 0
    # 左上
    for i in range(1, n):
        if i <= min(a - 1, b - 1):
            left[i] = 1
        else:
            left[i] = 0
    # 右上
    for i in range(1, n):
        if i <= min(a - 1, n - b):
            right[i] = 1
        else:
            right[i] = 0
    # 横向
    for i in range(1, n):
        if i <= min(a - 1, b - 1):
            row[i] = 1
        else:
            row[i] = 0
    # 纵向
    for i in range(1, n):
        if i <= b - 1:
            col[i] = 1
        else:
            col[i] = 0
    # 左上
    for i in range(1, n):
        if i <= min(a - 1, b - 1):
            left[i] = 1
