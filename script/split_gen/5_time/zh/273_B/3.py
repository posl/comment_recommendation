def problem273_b():
    x,k = map(int,input().split())
    for i in range(k):
        x = x//10*10+10
    print(x)
