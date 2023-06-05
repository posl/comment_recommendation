def problems108_c():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        if a%k == 0:
            ans += n//k
        else:
            ans += n//k + 1
    print(ans)
problems108_c()
