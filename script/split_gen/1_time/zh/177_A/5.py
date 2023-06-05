def problem177_a():
    # 输入
    D, T, S = map(int, input().split())
    # 处理
    if D / S <= T:
        print("Yes")
    else:
        print("No")
