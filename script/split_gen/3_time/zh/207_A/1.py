def problem207_a():
    #读取输入
    a,b,c = map(int,input().split())
    #计算输出
    print(max(a+b,b+c,c+a))
problem207_a()
