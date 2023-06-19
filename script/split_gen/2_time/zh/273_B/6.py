def problems273_b():
    x,k = map(int,input().split())
    for i in range(k):
        x = (x+5)//10*10
        if x%10 == 0:
            x = x//10
    print(x)
