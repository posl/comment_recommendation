def problems125_a():
    a,b,t = map(int,input().split())
    cnt = 0
    for i in range(1,t+1):
        if i%a==0:
            cnt += b
    print(cnt)
