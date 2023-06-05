def problem189_a():
    #读取输入
    C = input()
    #判断是否胜利
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")
