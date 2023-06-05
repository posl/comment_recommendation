def problem258_a():
    import sys
    # 读取输入
    K = int(sys.stdin.readline().strip())
    # 计算
    hour = 21 + (K // 60)
    min = K % 60
    # 输出
    print(str(hour).zfill(2) + ":" + str(min).zfill(2))

if __name__ == '__main__':
    problem258_a()