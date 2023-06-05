def dice():
    #输入骰子的三个面
    a,b,c = map(int, input().split())
    #输出骰子的底面的和
    print(21-a-b-c)
