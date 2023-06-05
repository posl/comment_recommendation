def main():
    # 读入输入
    s = list(input())
    q = int(input())
    # 倒序标志
    rev = 0
    # 从后向前读入
    for i in range(q):
        tmp = input().split()
        # 反转
        if tmp[0] == '1':
            rev = 1 - rev
        # 添加
        else:
            f = int(tmp[1])
            c = tmp[2]
            if (f == 1 and rev == 0) or (f == 2 and rev == 1):
                s.insert(0, c)
            else:
                s.append(c)
    # 结果
    if rev == 1:
        s.reverse()
    print(''.join(s))
