def problem273_b():
    x,k = map(int,input().split())
    for i in range(k):
        if x % 200 == 0:
            x = x // 200
        else:
            x = x * 1000 + 200
    print(x)
