def solve():
    # 读取输入
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 计算结果
    c = 0
    for i in range(n):
        if s[i] == 'For':
            c += 1
    # 输出结果
    if c > n / 2:
        print('Yes')
    else:
        print('No')
