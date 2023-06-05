def mymain():
    #读取输入
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    #计算
    ans = 0
    for i in range(n):
        if i%2 == 0:
            ans += max(a[i]-x,0)
        else:
            ans += a[i]
    #输出
    print(ans)
mymain()
