def main():
    import sys
    # 读取标准输入
    lines = sys.stdin.readlines()
    # 读取第一行
    line = lines[0].strip()
    # 按空格分割
    n, q = line.split()
    # 转换为整数
    n = int(n)
    q = int(q)
    # 读取第二行
    line = lines[1].strip()
    # 按空格分割
    x = line.split()
    # 转换为整数
    x = [int(i) for i in x]
    # 球的位置
    pos = [i for i in range(1, n + 1)]
    # 操作
    for i in range(q):
        # 球的位置
        p = pos[x[i] - 1]
        # 球的位置
        pos[x[i] - 1] = pos[x[i]]
        # 球的位置
        pos[x[i]] = p
        # 球的位置
        x[i] = x[i] + 1
    # 打印
    for i in range(n):
        print(pos[i], end=" ")

if __name__ == '__main__':
    main()