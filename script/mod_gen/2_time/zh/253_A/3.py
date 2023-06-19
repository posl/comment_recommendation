def median(a,b,c):
    if a<=b<=c or c<=b<=a:
        print("是")
    else:
        print("没有")
a,b,c = map(int,input().split())
median(a,b,c)
