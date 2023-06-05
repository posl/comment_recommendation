def solve(N,A):
    ans = 2**31
    for i in range(N):
        for j in range(i,N):
            x = 0
            for k in range(i,j+1):
                x = x | A[k]
            ans = min(ans,x)
    print(ans)
