def solve(n,k):
    mod=10**9+7
    sum=0
    for i in range(k,n+2):
        min=i*(i-1)//2
        max=i*(2*n-i+1)//2
        sum=(sum+max-min+1)%mod
    return sum
