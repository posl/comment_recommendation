def problems135_a():
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print((a+b)//2)
    else:
        print('IMPOSIBLE')
