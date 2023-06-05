def problem273_b():
    x,k = map(int,input().split())
    cur = x
    for i in range(k):
        cur = round(cur,-i)
    print(cur)
