def problem273_b():
    x,k = map(int,input().split())
    ans = x
    for i in range(k):
        ans = (ans+5)//10*10
    print(ans)
