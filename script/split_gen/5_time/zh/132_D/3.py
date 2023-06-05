def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = [0]*k
    for i in range(1,k+1):
        if i == 1:
            ans[i-1] = n-k+1
        else:
            ans[i-1] = (n-k+1)*(i-1)*(n-k+2-i)//(i*(i-1))%mod
    for i in range(k):
        print(ans[i])
